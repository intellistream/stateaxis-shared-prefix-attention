# Historical real-NPU component gates

These five JSON files are byte-for-byte copies of the frozen StateAxis issue
#13 preregistrations and results. `SHA256SUMS` reproduces the hashes listed in
`../ISSUE13_SHARED_PREFIX_ATTENTION_CLOSURE.md`.

The evidence is a component-level negative qualification result:

- V250 reduced component P50 from 650.724 us to 447.798 us (31.185%) but
  failed correctness (`max_abs_error=0.01477`, prefix LSE error `0.19936`);
- V262's dedicated correctness run passed at suffix lengths 130, 145, and
  161;
- V262's matched timing run did not preserve correctness: S130 and S145
  failed, and S145 produced non-finite output; and
- its P50 reductions were 14.063%, 12.974%, and 9.828%, all below the
  preregistered 20% crossover gate.

No candidate cleared correctness and performance together. The current
Manifest 0.3 MOD is therefore `telemetry_only` and does not dispatch these
historical device kernels. A service ON/OFF run of version 0.2.0 would measure
telemetry overhead, not shared-prefix attention acceleration.
