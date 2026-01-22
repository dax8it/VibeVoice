Upstream sync notes (2026-01-21)

Conflicts resolved (defaulted to upstream/theirs):
- pyproject.toml
- vibevoice/modular/modeling_vibevoice.py
- vibevoice/modular/modular_vibevoice_tokenizer.py

MPS/Metal notes:
- No MPS-specific overrides were required in the conflicted files.

Other:
- Local untracked models/ directory was excluded from stash to avoid large stash size.

ASR sync notes (2026-01-22)

Imported from upstream:
- Figures/VibeVoice_ASR_archi.png
- demo/vibevoice_asr_gradio_demo.py
- demo/vibevoice_asr_inference_from_file.py
- docs/vibevoice-asr.md
- vibevoice/modular/modeling_vibevoice_asr.py
- vibevoice/processor/vibevoice_asr_processor.py

Local adjustments:
- Enforced local-only model paths by default with ALLOW_REMOTE_MODEL_DOWNLOAD=1 opt-in.
- Added CUDA > MPS > CPU device selection and MPS-friendly dtype/attention defaults in ASR demos.
