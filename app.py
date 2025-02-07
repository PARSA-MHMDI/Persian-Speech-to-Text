import torch
import librosa
from espnet2.bin.asr_inference import Speech2Text
import gradio as gr


# def text_normalizer(text):
#    text = text.upper()
#    return text.translate(str.maketrans('', '', string.punctuation))

def inference(audio):
  lang = 'fa'
  fs = 16000

  speech2text = Speech2Text(
        asr_train_config="asr_config.yaml",
        asr_model_file="valid.acc.ave_10best.pth",
        lm_train_config="config.yaml",
        lm_file="lm_valid.loss.ave_10best.pth",
        lm_weight= 0.43,
        device="cpu",
        minlenratio=0.0,
        maxlenratio=0.0,
        ctc_weight=1,
        beam_size=1,
        batch_size=0,
        nbest=1
  )
  speech, rate = librosa.load(audio, sr=16000)
  assert rate == fs, "mismatch in sampling rate"
  nbests = speech2text(speech)
  text, *_ = nbests[0]
  # return f"ASR hypothesis: {text_normalizer(text)}"
  return str(text)

def upload_manage(upload,microphone):
    print(upload)
    print(microphone)
    if upload:
        result = inference(upload)
    elif microphone:
        result = inference(microphone)

    return result
        

inputs = [gr.inputs.Audio(source="upload",label="upload", type="filepath"),gr.inputs.Audio(source="microphone",label="microphone", type="filepath")]
outputs =  gr.outputs.Textbox(label="Output Text")

title = "Persian ASR / E-Branchformer"
description = "<p><center>This appication created by <strong>Parsa Mohammadi</strong>. <br> <br> <a href='https://github.com/PARSA-MHMDI'><strong>Github</strong></a> . <a href='https://www.linkedin.com/in/parsa-mohammadi-0b079620a/'><strong>LinkedIn</strong></a></center></p>"
gr.Interface(upload_manage, inputs, outputs, title=title, description=description, enable_queue=True).launch(debug=True)

