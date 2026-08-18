import runpod
import base64
# Importa la clase principal de inferencia de tu fork de LivePortrait
from src.pipelines.live_portrait_pipeline import LivePortraitPipeline
from src.config.inference_config import InferenceConfig

# Inicialización global para evitar recargar pesos en cada request (mitiga cold starts)
config = InferenceConfig()
pipeline = LivePortraitPipeline(inference_cfg=config)

def handler(job):
    job_input = job['input']
    source_image_b64 = job_input.get('source_image')
    driving_video_b64 = job_input.get('driving_video')
    
    # 1. Decodificar base64 a archivos temporales
    # 2. Ejecutar inferencia: pipeline.execute(source_path, driving_path)
    # 3. Codificar resultado a base64
    
    return {"video_base64": "resultado_codificado"}

runpod.serverless.start({"handler": handler})
