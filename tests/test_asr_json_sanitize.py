import json

from vibevoice.processor.vibevoice_asr_processor import sanitize_asr_json_output


def test_sanitize_asr_json_output_with_assistant_prefix():
    raw = "assistant\n[ {\"Speaker ID\": \"A\", \"Start time\": 0.0, \"End time\": 1.0, \"Content\": \"hello\"} ]"
    cleaned = sanitize_asr_json_output(raw)
    result = json.loads(cleaned)

    assert isinstance(result, list)
    assert result[0]["Speaker ID"] == "A"
