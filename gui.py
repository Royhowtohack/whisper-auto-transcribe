# %%
language_list = [
    "auto",
    "english",
    "chinese",
    "japanese",
    "korean",
    "german",
    "spanish",
    "russian",
    "french",
    "portuguese",
    "turkish",
    "polish",
    "catalan",
    "dutch",
    "arabic",
    "swedish",
    "italian",
    "indonesian",
    "hindi",
    "finnish",
    "vietnamese",
    "hebrew",
    "ukrainian",
    "greek",
    "malay",
    "czech",
    "romanian",
    "danish",
    "hungarian",
    "tamil",
    "norwegian",
    "thai",
    "urdu",
    "croatian",
    "bulgarian",
    "lithuanian",
    "latin",
    "maori",
    "malayalam",
    "welsh",
    "slovak",
    "telugu",
    "persian",
    "latvian",
    "bengali",
    "serbian",
    "azerbaijani",
    "slovenian",
    "kannada",
    "estonian",
    "macedonian",
    "breton",
    "basque",
    "icelandic",
    "armenian",
    "nepali",
    "mongolian",
    "bosnian",
    "kazakh",
    "albanian",
    "swahili",
    "galician",
    "marathi",
    "punjabi",
    "sinhala",
    "khmer",
    "shona",
    "yoruba",
    "somali",
    "afrikaans",
    "occitan",
    "georgian",
    "belarusian",
    "tajik",
    "sindhi",
    "gujarati",
    "amharic",
    "yiddish",
    "lao",
    "uzbek",
    "faroese",
    "haitian creole",
    "pashto",
    "turkmen",
    "nynorsk",
    "maltese",
    "sanskrit",
    "luxembourgish",
    "myanmar",
    "tibetan",
    "tagalog",
    "malagasy",
    "assamese",
    "tatar",
    "hawaiian",
    "lingala",
    "hausa",
    "bashkir",
    "javanese",
    "sundanese",
]

language_list = [x.title() for x in language_list]
language_list

language_key_list = [
    "auto",
    "en",
    "zh",
    "ja",
    "ko",
    "de",
    "es",
    "ru",
    "fr",
    "pt",
    "tr",
    "pl",
    "ca",
    "nl",
    "ar",
    "sv",
    "it",
    "id",
    "hi",
    "fi",
    "vi",
    "iw",
    "uk",
    "el",
    "ms",
    "cs",
    "ro",
    "da",
    "hu",
    "ta",
    "no",
    "th",
    "ur",
    "hr",
    "bg",
    "lt",
    "la",
    "mi",
    "ml",
    "cy",
    "sk",
    "te",
    "fa",
    "lv",
    "bn",
    "sr",
    "az",
    "sl",
    "kn",
    "et",
    "mk",
    "br",
    "eu",
    "is",
    "hy",
    "ne",
    "mn",
    "bs",
    "kk",
    "sq",
    "sw",
    "gl",
    "mr",
    "pa",
    "si",
    "km",
    "sn",
    "yo",
    "so",
    "af",
    "oc",
    "ka",
    "be",
    "tg",
    "sd",
    "gu",
    "am",
    "yi",
    "lo",
    "uz",
    "fo",
    "ht",
    "ps",
    "tk",
    "nn",
    "mt",
    "sa",
    "lb",
    "my",
    "bo",
    "tl",
    "mg",
    "as",
    "tt",
    "haw",
    "ln",
    "ha",
    "ba",
    "jw",
    "su",
]

speed_list = ["large", "medium", "small", "base", "tiny"]

# %%
from multiprocessing.sharedctypes import Value
import whisper
import datetime
import torch
from time import gmtime, strftime


def transcribe_start(model_type, file_path, language_input):
    # print(model_type, file_path, language_input)
    language = None if language_input == "auto" else language_input

    model = whisper.load_model(model_type)

    print(model.device)

    result = model.transcribe(file_path, language=language)
    # print(result["text"])
    path = "{}.srt".format(strftime("%Y%m%d-%H%M%S", gmtime()))
    # print(__file__)
    with open(path, "w", encoding="UTF-8") as f:
        for seg in result["segments"]:
            id = seg["id"]
            start = (
                str(datetime.timedelta(seconds=round(seg["start"])))
                + ","
                + str(seg["start"] % 1)[2:5]
            )
            end = (
                str(datetime.timedelta(seconds=round(seg["end"])))
                + ","
                + str(seg["end"] % 1)[2:5]
            )
            text = seg["text"]
            f.write(f"{id}\n{start} --> {end}\n{text}\n\n")

    del result
    del model
    torch.cuda.empty_cache()

    return path


# %%
from operator import truediv
from tkinter.tix import Tree
import gradio as gr


def change_type(file_type):
    if file_type == "Video":
        return [gr.update(visible=True), gr.update(visible=False)]
    elif file_type == "Audio":
        return [gr.update(visible=False), gr.update(visible=True)]


def transcribe_submit(language, speed, file_type, video_input, audio_input):
    output_type = [None, None]
    if file_type == "Video":
        # output_type = [
        #     gr.update(value=video_input, visible=True),
        #     gr.update(visible=False),
        # ]
        input_file = video_input
    elif file_type == "Audio":
        # output_type = [
        #     gr.update(visible=False),
        #     gr.update(value=audio_input, visible=True),
        # ]
        input_file = audio_input

    # print(",".join([language_key_list[language], speed_list[speed], file_type]))

    srt_path = transcribe_start(
        speed_list[speed - 1], input_file, language_key_list[language]
    )

    return output_type + [
        gr.update(value="Done", visible=True),
        gr.update(value=srt_path, visible=True),
    ]


with gr.Blocks() as demo:
    with gr.Row():
        language = gr.Dropdown(
            label="Language",
            value="Auto",
            choices=language_list,
            type="index",
            interactive=True,
        )

        speed = gr.Slider(
            minimum=1,
            maximum=5,
            step=1,
            interactive=True,
            label="Speed",
        )

        file_type = gr.Radio(
            ["Video", "Audio"],
            value="Video",
            label="File Type",
            interactive=True,
        )
    with gr.Row():
        with gr.Column():
            video_input = gr.Video(
                label="Video File", interactive=True, mirror_webcam=False
            )
            audio_input = gr.Audio(label="Audio File", interactive=True, visible=False)
            submit_btn = gr.Button("Transcribe")

    with gr.Row():
        with gr.Column():
            video_output = gr.Video(label="Demo", interactive=False, visible=False)
            audio_output = gr.Audio(label="Demo", interactive=False, visible=False)
            subtitle_output = gr.Text(
                label="Demo",
                value="Drag the file and Transcribe!",
                interactive=False,
                visible=True,
            )
            srt_output = gr.File(interactive=False, visible=False)

    file_type.change(
        fn=change_type,
        inputs=[file_type],
        outputs=[video_input, audio_input],
    )

    submit_btn.click(
        fn=transcribe_submit,
        inputs=[language, speed, file_type, video_input, audio_input],
        outputs=[video_output, audio_output, subtitle_output, srt_output],
    )

    # demo_play.play()

demo.launch()

# %%
