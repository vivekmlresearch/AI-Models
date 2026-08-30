## **Best Time Series Models**


## 1. TimesFM

TimesFM is a pretrained foundation model for time-series forecasting. The key idea is zero-shot forecasting: you can give it a historical sequence (context), and it produces future values without training a custom model for your dataset. Google Research introduced it as a decoder-only Transformer specialized for time series, and reported that despite being much smaller than large language models—it can achieve near state of the art accuracy on multiple unseen forecasting benchmarks.

TimesFM aims to reduce that friction:

One general model that works across domains and granularities,

Zero-shot performance that can be competitive with supervised models trained per dataset,

Option to operationalize it as a reusable forecasting component in data platforms (e.g., BigQuery).

**Core capabilities**

1) Zero-shot forecasting:- TimesFM is designed to forecast accurately on previously unseen datasets without retraining.

2) Works across different horizons and granularities: The paper/blog emphasize flexibility across history length, forecast horizon, and time granularity at inference time.

3) Univariate forecasting focus:- TimesFM’s common public interface is univariate: you provide one target series (optionally with a frequency indicator), and it predicts future points.

**Model architecture (high level)**

Decoder-only Transformer (time-series specific):- TimesFM is built as a decoder-only Transformer (similar in shape to GPT-style decoders, but trained for numeric sequences).

“Patched” / segment-based processing:- Instead of predicting one point at a time naïvely, TimesFM is described as outputting batches of contiguous time-point segments and using a “patched-decoder style attention” design.

Why patching helps: time series can be long; patching/segmenting can reduce effective sequence length and help the model capture multi-scale patterns (trend/seasonality/local fluctuations) more efficiently than raw point-by-point attention.

Training data and scale:- pretraining on roughly O(100B) time points with a ~200M parameter model.


Datasets:- Google Trends

TimesFM Config:-

<img width="483" height="397" alt="image" src="https://github.com/user-attachments/assets/e241ad7f-bcc2-4258-b183-1e2893405ea4" />

Preditions Results:-

<img width="1037" height="363" alt="image" src="https://github.com/user-attachments/assets/a7244a70-5dc5-4881-a393-012e5611cda6" />

References:-

    1.https://arxiv.org/abs/2310.10688
    2.https://github.com/google-research/timesfm
    3.https://huggingface.co/google/timesfm-1.0-200m


---


