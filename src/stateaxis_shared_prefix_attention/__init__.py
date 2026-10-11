"""Exact activation contract for shared-prefix attention admission."""

from __future__ import annotations

from dataclasses import dataclass

MOD_ID = "org.vllm-hust.stateaxis-shared-prefix-attention"


@dataclass(frozen=True, slots=True)
class SharedPrefixAttentionConfig:
    """The only shared-prefix cohort admission contract accepted by StateAxis."""

    enabled: bool = True
    telemetry_only: bool = True
    max_group_size: int = 32
    min_group_size: int = 2
    block_tokens: int = 128
    require_decode: bool = True
    require_same_state_generation: bool = True
    require_full_block_prefix: bool = True
    require_same_context_length: bool = True
    stable_member_order: bool = True
    fallback_to_paged_attention: bool = True
    extend_state_lifetime: bool = False
    fail_closed: bool = True

    def __post_init__(self) -> None:
        if self != SharedPrefixAttentionConfig.__new_default():
            raise ValueError("shared-prefix attention requires the reviewed contract")

    @classmethod
    def __new_default(cls) -> SharedPrefixAttentionConfig:
        instance = object.__new__(cls)
        values = {
            "enabled": True,
            "telemetry_only": True,
            "max_group_size": 32,
            "min_group_size": 2,
            "block_tokens": 128,
            "require_decode": True,
            "require_same_state_generation": True,
            "require_full_block_prefix": True,
            "require_same_context_length": True,
            "stable_member_order": True,
            "fallback_to_paged_attention": True,
            "extend_state_lifetime": False,
            "fail_closed": True,
        }
        for field, value in values.items():
            object.__setattr__(instance, field, value)
        return instance


def shared_prefix_attention() -> SharedPrefixAttentionConfig:
    """Return the default-off candidate's admitted ON configuration."""

    return SharedPrefixAttentionConfig()


__all__ = ["MOD_ID", "SharedPrefixAttentionConfig", "shared_prefix_attention"]
