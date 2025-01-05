"""
Constants for the rysk package.
"""

import os
from dataclasses import dataclass

from citrex.enums import Environment, SupportedChains

REFERRAL_CODE = os.environ.get("citrex_REFERRAL_CODE", "macchiadisugo")


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
        return "ciao"


CONFIG = {
    SupportedChains.SEI: {
        Environment.PROD: EnvConfig(
            "https://api.citrex.markets/v1",
            "wss://api.citrex.markets/v1/ws/operate",
            os.environ.get("citrex_RPC_URL", "https://evm-rpc.sei-apis.com"),
            1329,
            "0x3894085Ef7Ff0f0aeDf52E2A2704928d1Ec074F1",
            "0x7461cFe1A4766146cAFce60F6907Ea657550670d",
            "0x993543DC8BdFCba9fc7355d822108eF49dB6b9F9",
        ),
        Environment.TESTNET: EnvConfig(
            "https://api.staging.citrex.markets/v1",
            "wss://api.staging.citrex.markets/v1/ws/operate",
            os.environ.get("citrex_RPC_URL", "https://evm-rpc-testnet.sei-apis.com"),
            1328,
            "0x79A59c326C715AC2d31C169C85d1232319E341ce",
            "0x0F571400ef7D2aEc68b29e58be3adCE1Bb27f33d",
            "0x24f4e9Db8225e6AE220FE89782E4A010aEB7bb14",
        ),
    },
    SupportedChains.ARBITRUM: {
        Environment.PROD: EnvConfig(
            "https://arbitrum-api.prod.rysk.finance",
            "wss://arbitrum-stream.prod.rysk.finance",
            os.environ.get("rysk_v2_RPC_URL", "https://arb1.arbitrum.io/rpc"),
            42161,
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000",
        ),
        Environment.TESTNET: EnvConfig(
            "https://arbitrum-api.staging.rysk.finance",
            "wss://arbitrum-stream.staging.rysk.finance",
            os.environ.get("rysk_v2_RPC_URL", "https://sepolia-rollup.arbitrum.io/rpc"),
            421614,
            "0xb8bE1401E65dC08Bfb8f832Fc1A27a16CA821B05",
            "0x71728FDDF90233cc35D61bec7858d7c42A310ACe",
            "0x27809a3Bd3cf44d855f1BE668bFD16D34bcE157C",
        ),
    },
    SupportedChains.BLAST: {
        Environment.PROD: EnvConfig(
            "https://api.100x.finance",
            "wss://stream.100x.finance",
            os.environ.get("rysk_v2_RPC_URL", "https://rpc.blast.io"),
            81457,
            "0x4300000000000000000000000000000000000003",
            "0x1BaEbEE6B00B3f559B0Ff0719B47E0aF22A6bfC4",
            "0x691a5fc3a81a144e36c6C4fBCa1fC82843c80d0d",
        ),
        Environment.TESTNET: EnvConfig(
            "https://api.staging.100x.finance",
            "wss://stream.staging.100x.finance",
            os.environ.get("rysk_v2_RPC_URL", "https://sepolia.blast.io"),
            168587773,
            "0x79A59c326C715AC2d31C169C85d1232319E341ce",
            "0x9645aD4bE9bAd73B95ae785765e3683e418806A9",
            "0xb87e7d837844F3BbbF043F47E6Ee15B42208F9cd",
        ),
    },
    SupportedChains.CUSTOM: {
        Environment.DEVNET: EnvConfig(
            os.environ.get("citrex_API_URL"),
            os.environ.get("citrex_STREAM_URL"),
            os.environ.get("citrex_RPC_URL"),
            int(os.environ.get("citrex_CHAIN_ID", 0)),
            os.environ.get("citrex_CORE_COLLATERAL"),
            os.environ.get("citrex_PROTOCOL"),
            os.environ.get("citrex_VERIFYING_CONTRACT"),
        ),
    },
}
