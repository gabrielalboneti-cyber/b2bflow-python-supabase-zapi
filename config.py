import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:
    supabase_url: str
    supabase_key: str
    zapi_instance_id: str
    zapi_instance_token: str
    zapi_client_token: str

    @classmethod
    def from_env(cls):
        load_dotenv()

        config = cls(
            supabase_url=os.getenv("SUPABASE_URL", ""),
            supabase_key=os.getenv("SUPABASE_KEY", ""),
            zapi_instance_id=os.getenv("ZAPI_INSTANCE_ID", ""),
            zapi_instance_token=os.getenv("ZAPI_INSTANCE_TOKEN", ""),
            zapi_client_token=os.getenv("ZAPI_CLIENT_TOKEN", ""),
        )

        config.validate()
        return config

    def validate(self):
        missing = [
            name
            for name, value in {
                "SUPABASE_URL": self.supabase_url,
                "SUPABASE_KEY": self.supabase_key,
                "ZAPI_INSTANCE_ID": self.zapi_instance_id,
                "ZAPI_INSTANCE_TOKEN": self.zapi_instance_token,
                "ZAPI_CLIENT_TOKEN": self.zapi_client_token,
            }.items()
            if not value
        ]

        if missing:
            raise ValueError(
                "Variáveis de ambiente obrigatórias não configuradas: "
                + ", ".join(missing)
            )

    @property
    def zapi_url(self):
        return (
            "https://api.z-api.io/instances/"
            f"{self.zapi_instance_id}/token/"
            f"{self.zapi_instance_token}/send-text"
        )
