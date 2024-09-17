"""
Constants for the rysk package.
"""

import os
from dataclasses import dataclass

from rysk_v2.enums import Environment, SupportedChains

REFERRAL_CODE = os.environ.get("RYSK_V2_REFERRAL_CODE", "macchiadisugo")


@dataclass(frozen=True)
class EnvConfig:
    api_url: str
    stream_url: str
    rpc_url: str
    chain_id: int
    core_collateral: str
    protocol: str
    verifying_contract: str

    def check(self):
        return all(
            [
                self.api_url,
                self.stream_url,
                self.rpc_url,
                self.chain_id,
                self.core_collateral,
                self.protocol,
                self.verifying_contract,
            ]
        )

    @property
    def eip712_domain_name(self):
        """
        return the correct eip712 domain name for signing
        """
        return self.api_url.split('.')[-2]


CONFIG = {
    SupportedChains.ARBITRUM: {
        Environment.PROD: EnvConfig(
            "https://api-arbitrum.prod.rysk.finance",
            "wss://stream-arbitrum.prod.rysk.finance",
            os.environ.get("RYSK_V2_RPC_URL", "https://arb1.arbitrum.io/rpc"),
            42161,
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000",
        ),
        Environment.TESTNET: EnvConfig(
            "https://api-arbitrum.staging.rysk.finance",
            "wss://stream-arbitrum.staging.rysk.finance",
            os.environ.get("RYSK_V2_RPC_URL", "https://sepolia-rollup.arbitrum.io/rpc"),
            421614,
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000",
        ),
    },
    SupportedChains.BLAST: {
        Environment.PROD: EnvConfig(
            "https://api.100x.finance",
            "wss://stream.100x.finance",
            os.environ.get("RYSK_V2_RPC_URL", "https://rpc.blast.io"),
            81457,
            "0x4300000000000000000000000000000000000003",
            "0x1BaEbEE6B00B3f559B0Ff0719B47E0aF22A6bfC4",
            "0x691a5fc3a81a144e36c6C4fBCa1fC82843c80d0d",
        ),
        Environment.TESTNET: EnvConfig(
            "https://api.staging.100x.finance",
            "wss://stream.staging.100x.finance",
            os.environ.get("RYSK_V2_RPC_URL", "https://sepolia.blast.io"),
            168587773,
            "0x79A59c326C715AC2d31C169C85d1232319E341ce",
            "0x9645aD4bE9bAd73B95ae785765e3683e418806A9",
            "0xb87e7d837844F3BbbF043F47E6Ee15B42208F9cd",
        ),
    },
    SupportedChains.CUSTOM: {
        Environment.DEVNET: EnvConfig(
            os.environ.get("RYSK_V2_API_URL"),
            os.environ.get("RYSK_V2_STREAM_URL"),
            os.environ.get("RYSK_V2_RPC_URL"),
            int(os.environ.get("RYSK_V2_CHAIN_ID", 0)),
            os.environ.get("RYSK_V2_CORE_COLLATERAL"),
            os.environ.get("RYSK_V2_PROTOCOL"),
            os.environ.get("RYSK_V2_VERIFYING_CONTRACT"),
        ),
    },
}
