# Issue #13: exact shared-prefix attention closure

> **Document role: point-in-time report, not current repository status or a task
> assignment.** Current classification and priorities live only in
> [`NATIVE_ENGINE_STATUS.md`](../../NATIVE_ENGINE_STATUS.md).

Issue #13 is closed as a real-hardware component negative result. It is not a production serving optimization and is not enabled by default.

## Evidence audit

The V250 B32 shared-prefix component on NPU 4 reduced component P50 from 650.724 µs to 447.798 µs (31.185%), but failed its unchanged correctness gate: final max absolute error was 0.01477 and prefix LSE max error was 0.19936. This result is rejected despite its performance shape.

The later V262 endpoint work separated correctness and timing. Its dedicated NPU correctness run passed for suffix lengths 130, 145, and 161, with max output errors from 0.000440 to 0.000485, max LSE error 9.54e-7, and zero padding-invariance error. The matched timing run did not preserve that result: S130 and S145 failed correctness (S145 produced non-finite output), and measured P50 reductions were only 14.063%, 12.974%, and 9.828%. Every endpoint missed the preregistered 20% reduction target, so both correctness and performance gates failed.

The repository has project-owned PTO component exports and CPU reference tests, but no `shared_prefix_group` in the Rust scheduler/runtime and no `StatecentricQwen14bSharedPrefixPtoLaunch` binding in the resident worker. Consequently there is no production candidate authority or serving runner to evaluate without adding a new worker ABI, descriptor, generation-safe grouping contract, execution artifact, and state namespace. A component timing result cannot be promoted to an HTTP serving claim.

## Decision

- Preserve all accepted and rejected component evidence.
- Do not integrate V250/V262 into the resident worker.
- Do not claim request throughput, output-token throughput, HBM, or vLLM-HUST superiority.
- Keep ordinary paged attention authoritative.
- Close Issue #13 under its explicit negative-exit clause: no portable exact path cleared both correctness and crossover gates.

## Frozen evidence hashes

- V250 rejected result: `9e6188d99807cfffd4f0e7d199b79217cf4df4ad81bdb24c9f2614d547bf0b44`
- V262 accepted correctness result: `373299f0ebef4e28768bf528e5532684797c33388a31d03f169e96ba8a60ddea`
- V262 rejected timing result: `d99e8dab93f00a9552800c3b2d6f481c775cc96e5596ffae3dee8c6f230526c7`
- V250 preregistration: `df50060254f65670b4a6a35fab74c87f0055ba132fbbbed4fcbae87466b82465`
- V262 timing preregistration: `fc1f76ff5bdf4959473d5feaea71568b699b60603ed7108bc37c29b318d82215`
