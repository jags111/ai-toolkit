
import torch
from toolkit.config_modules import GenerateImageConfig, ModelConfig
from toolkit.models.base_model import BaseModel
from toolkit.prompt_utils import PromptEmbeds
from diffusers import AutoencoderKLWan, WanTransformer3DModel, WanPipeline

class Wan21(BaseModel):
    def __init__(
            self,
            device,
            model_config: ModelConfig,
            dtype='bf16',
            custom_pipeline=None,
            noise_scheduler=None,
            **kwargs
    ):
        super().__init__(device, model_config, dtype,
                         custom_pipeline, noise_scheduler, **kwargs)
        self.is_flow_matching = True
    # these must be implemented in child classes

    def load_model(self):
        # override this in child classes
        raise NotImplementedError(
            "load_model must be implemented in child classes")

    def get_generation_pipeline(self):
        # override this in child classes
        raise NotImplementedError(
            "get_generation_pipeline must be implemented in child classes")

    def generate_single_image(
        self,
        gen_config: GenerateImageConfig,
        conditional_embeds: PromptEmbeds,
        unconditional_embeds: PromptEmbeds,
        generator: torch.Generator,
        extra: dict,
    ):
        # override this in child classes
        raise NotImplementedError(
            "generate_single_image must be implemented in child classes")

    def get_noise_prediction(
        latent_model_input: torch.Tensor,
        timestep: torch.Tensor,  # 0 to 1000 scale
        text_embeddings: PromptEmbeds,
        **kwargs
    ):
        raise NotImplementedError(
            "get_noise_prediction must be implemented in child classes")

    def get_prompt_embeds(self, prompt: str) -> PromptEmbeds:
        raise NotImplementedError(
            "get_prompt_embeds must be implemented in child classes")
