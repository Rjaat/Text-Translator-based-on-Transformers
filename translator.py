# translator.py
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import json
import os

# Function to fetch available translation models
def fetch_translation_models():
    models = {
        "en_to_fr": "Helsinki-NLP/opus-mt-en-fr",
        "fr_to_en": "Helsinki-NLP/opus-mt-fr-en",
        "en_to_de": "Helsinki-NLP/opus-mt-en-de",
        "de_to_en": "Helsinki-NLP/opus-mt-de-en",
        "en_to_es": "Helsinki-NLP/opus-mt-en-es",
        "es_to_en": "Helsinki-NLP/opus-mt-es-en",
        "en_to_it": "Helsinki-NLP/opus-mt-en-it",
        "it_to_en": "Helsinki-NLP/opus-mt-it-en",
        "en_to_ru": "Helsinki-NLP/opus-mt-en-ru",
        "ru_to_en": "Helsinki-NLP/opus-mt-ru-en",
        "en_to_zh": "Helsinki-NLP/opus-mt-en-zh",
        "zh_to_en": "Helsinki-NLP/opus-mt-zh-en",
        "en_to_ar": "Helsinki-NLP/opus-mt-en-ar",
        "ar_to_en": "Helsinki-NLP/opus-mt-ar-en",
        #"en_to_pt": "Helsinki-NLP/opus-mt-en-pt",
        #"pt_to_en": "Helsinki-NLP/opus-mt-pt-en",
        # "en_to_ja": "Helsinki-NLP/opus-mt-en-ja",
        # "ja_to_en": "Helsinki-NLP/opus-mt-ja-en",
        # "en_to_nl": "Helsinki-NLP/opus-mt-en-nl",
        # "nl_to_en": "Helsinki-NLP/opus-mt-nl-en",
        # "en_to_sv": "Helsinki-NLP/opus-mt-en-sv",
        # "sv_to_en": "Helsinki-NLP/opus-mt-sv-en",
        # "en_to_fi": "Helsinki-NLP/opus-mt-en-fi",
        # "fi_to_en": "Helsinki-NLP/opus-mt-fi-en",
        # "en_to_no": "Helsinki-NLP/opus-mt-en-no",
        # "no_to_en": "Helsinki-NLP/opus-mt-no-en",
        # "en_to_da": "Helsinki-NLP/opus-mt-en-da",
        # "da_to_en": "Helsinki-NLP/opus-mt-da-en",
        # "en_to_tr": "Helsinki-NLP/opus-mt-en-tr",
        # "tr_to_en": "Helsinki-NLP/opus-mt-tr-en",
        # "en_to_pl": "Helsinki-NLP/opus-mt-en-pl",
        # "pl_to_en": "Helsinki-NLP/opus-mt-pl-en",
        # "en_to_cs": "Helsinki-NLP/opus-mt-en-cs",
        # "cs_to_en": "Helsinki-NLP/opus-mt-cs-en",
        # "en_to_sk": "Helsinki-NLP/opus-mt-en-sk",
        # "sk_to_en": "Helsinki-NLP/opus-mt-sk-en",
        # "en_to_hu": "Helsinki-NLP/opus-mt-en-hu",
        # "hu_to_en": "Helsinki-NLP/opus-mt-hu-en",
        # "en_to_et": "Helsinki-NLP/opus-mt-en-et",
        # "et_to_en": "Helsinki-NLP/opus-mt-et-en",
        # "en_to_lt": "Helsinki-NLP/opus-mt-en-lt",
        # "lt_to_en": "Helsinki-NLP/opus-mt-lt-en",
        # "en_to_lv": "Helsinki-NLP/opus-mt-en-lv",
        # "lv_to_en": "Helsinki-NLP/opus-mt-lv-en",
        # "en_to_ro": "Helsinki-NLP/opus-mt-en-ro",
        # "ro_to_en": "Helsinki-NLP/opus-mt-ro-en",
        # "en_to_bg": "Helsinki-NLP/opus-mt-en-bg",
        # "bg_to_en": "Helsinki-NLP/opus-mt-bg-en",
        # "en_to_sl": "Helsinki-NLP/opus-mt-en-sl",
        # "sl_to_en": "Helsinki-NLP/opus-mt-sl-en",
        # "en_to_hr": "Helsinki-NLP/opus-mt-en-hr",
        # "hr_to_en": "Helsinki-NLP/opus-mt-hr-en",
        # "en_to_sr": "Helsinki-NLP/opus-mt-en-sr",
        # "sr_to_en": "Helsinki-NLP/opus-mt-sr-en",
        # "en_to_mk": "Helsinki-NLP/opus-mt-en-mk",
        # "mk_to_en": "Helsinki-NLP/opus-mt-mk-en",
        # "en_to_bs": "Helsinki-NLP/opus-mt-en-bs",
        # "bs_to_en": "Helsinki-NLP/opus-mt-bs-en",
        # "en_to_is": "Helsinki-NLP/opus-mt-en-is",
        # "is_to_en": "Helsinki-NLP/opus-mt-is-en",
        # "en_to_ga": "Helsinki-NLP/opus-mt-en-ga",
        # "ga_to_en": "Helsinki-NLP/opus-mt-ga-en",
        # "en_to_mt": "Helsinki-NLP/opus-mt-en-mt",
        # "mt_to_en": "Helsinki-NLP/opus-mt-mt-en",
        # "en_to_he": "Helsinki-NLP/opus-mt-en-he",
        # "he_to_en": "Helsinki-NLP/opus-mt-he-en",
        # "en_to_el": "Helsinki-NLP/opus-mt-en-el",
        # "el_to_en": "Helsinki-NLP/opus-mt-el-en",
        # "en_to_vi": "Helsinki-NLP/opus-mt-en-vi",
        # "vi_to_en": "Helsinki-NLP/opus-mt-vi-en",
        # "en_to_th": "Helsinki-NLP/opus-mt-en-th",
        # "th_to_en": "Helsinki-NLP/opus-mt-th-en",
        "en_to_hi": "Helsinki-NLP/opus-mt-en-hi",
        # "hi_to_en": "Helsinki-NLP/opus-mt-hi-en",
        # "en_to_ur": "Helsinki-NLP/opus-mt-en-ur",
        # "ur_to_en": "Helsinki-NLP/opus-mt-ur-en",
        # "en_to_bn": "Helsinki-NLP/opus-mt-en-bn",
        # "bn_to_en": "Helsinki-NLP/opus-mt-bn-en",
        # "en_to_ta": "Helsinki-NLP/opus-mt-en-ta",
        # "ta_to_en": "Helsinki-NLP/opus-mt-ta-en",
        # "en_to_ml": "Helsinki-NLP/opus-mt-en-ml",
        # "ml_to_en": "Helsinki-NLP/opus-mt-ml-en",
        # "en_to_te": "Helsinki-NLP/opus-mt-en-te",
        # "te_to_en": "Helsinki-NLP/opus-mt-te-en",
        # "en_to_gu": "Helsinki-NLP/opus-mt-en-gu",
        # "gu_to_en": "Helsinki-NLP/opus-mt-gu-en",
        # "en_to_kn": "Helsinki-NLP/opus-mt-en-kn",
        # "kn_to_en": "Helsinki-NLP/opus-mt-kn-en",
        # "en_to_mr": "Helsinki-NLP/opus-mt-en-mr",
        # "mr_to_en": "Helsinki-NLP/opus-mt-mr-en",
        # "en_to_pa": "Helsinki-NLP/opus-mt-en-pa",
        # "pa_to_en": "Helsinki-NLP/opus-mt-pa-en",
        # "en_to_si": "Helsinki-NLP/opus-mt-en-si",
        # "si_to_en": "Helsinki-NLP/opus-mt-si-en",
        # "en_to_tl": "Helsinki-NLP/opus-mt-en-tl",
        # "tl_to_en": "Helsinki-NLP/opus-mt-tl-en",
        # "en_to_ceb": "Helsinki-NLP/opus-mt-en-ceb",
        # "ceb_to_en": "Helsinki-NLP/opus-mt-ceb-en",
        # "en_to_jw": "Helsinki-NLP/opus-mt-en-jw",
        # "jw_to_en": "Helsinki-NLP/opus-mt-jw-en",
        # "en_to_su": "Helsinki-NLP/opus-mt-en-su",
        # "su_to_en": "Helsinki-NLP/opus-mt-su-en",
    }
    return models



# Load translation pipelines
def load_translation_pipelines():
    models = fetch_translation_models()
    pipelines = {k: pipeline("translation", model=v) for k, v in models.items()}
    return pipelines

translation_pipelines = load_translation_pipelines()

def translate_text(text, model_key):
    # Get the correct translation pipeline
    translator = translation_pipelines.get(model_key)
    if translator:
        # Translate the text
        translated_text = translator(text, max_length=40)[0]['translation_text']
        return translated_text
    else:
        return "Model not found. Please check the language pair."

if __name__ == "__main__":
    # Example usage
    text = "Hello, how are you?"
    model_key = "translation_en_to_fr"
    print(translate_text(text, model_key))
