# DAY13 completion implementation plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task-by-task. Review the whole change independently before the final push.

**Goal:** Integrate all submitted branches and complete code/report coverage of the existing Lab 13 rubric.

**Architecture:** Keep the existing Python analysis entry point and CSV inputs. Add missing E1 calculations to the same reproducible output, reconcile the event contract, and shorten the launch/group reports to their required scope.

**Tech Stack:** Python 3.10+, pandas, scipy/statsmodels, PyYAML, unittest; Markdown/YAML reports.

**Spec:** `README.md`, `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`, `docs/du_lieu_va_cong_thuc.md`.

## Global constraints

- Preserve both CSVs, `src/lab13_starter.py`, the individual report template and the two committed independent label columns.
- All figures derived from `_simulated` minutes carry `simulated`; label cost ratios as well as absolute costs.
- A1 must pass before A/B/D/E calculations; all report figures are reproducible from code or an explicit calculation.
- Keep real names, contributions and attestations from the member branches; do not invent council results, signatures or LMS submission.
- Continue in the current checkout/main as in the already authorized workflow; no additional worktree or new product design is needed for this rubric completion.

## Review focus

- No reviewed requests: skip/override rate is unavailable rather than zero or a crash.
- Unreviewed rows must never enter the review-decision numerator or denominator.
- Display all three E1 numerators/denominators in the CLI output, not only in handwritten tables.
- Every proposed metric and failure mitigation must have observable events, timestamps and stable request joins.
- Planned pilot limits, sample maturity and final decision conditions must agree across YAML and launch/group reports.

## Task 1 · Integrate submitted work

**Files:** `TEAM.md`, TV4 personal report, cost/error/metric/launch/group reports.
**Interfaces:** consumes origin/main and origin/truien; produces one branch with four named members and all contributions.

- [x] Pull main, fetch all remote branches, inspect differences and preserve both histories.
- [x] Merge TV4 branch, retain TV3 contribution history and row, identify missing E1 code and conflicting event vocabularies.
- [x] Baseline: 9 unittest checks passed before implementation; merge commit `8f86b35`.

## Task 2 · Reproducible metrics and output

**Files:** modify `src/lab13.py`, `tests/test_lab13.py`; regenerate `report/team/TV1_ket_qua.txt`.
**Interfaces:** `tinh_e1(reqs) -> list[dict]` with `chi_so`, `tu_so`, `mau_so`, `ty_le`; `tong_hop` exports `e1`; CLI prints E1.

- [x] Write tests with literals 994/1200, 48/177, 51/1200; synthetic empty/no-review and unreviewed-decision cases; CLI runs and writes UTF-8 output.
- [x] Observe missing behavior fail, implement minimal pure metric aggregation and wire it into the CLI.
- [x] Run the complete unittest suite and regenerate output; package with documentation after final review.

## Task 3 · Reconcile and validate the submission bundle

**Files:** cost/error/metric/launch/group reports, `pilot_plan.yaml`, `TEAM.md`, personal report audit notes, `src/README.md`, `report/team/nghiem_thu.md`.
**Interfaces:** consumes Task 2 output and submitted labels; produces consistent documents and an evidence matrix.

- [x] Unify observable event names, identity/deduplication and maturity; retain both TV3/TV4 metric proposals, clearly defined.
- [x] Fix simulated-minute wording/labels, cost denominator explanations and measured failure detection thresholds.
- [x] Declare the two-attempt proposal consistently, keep the original three-attempt retrospective tables distinct, and make sample collection policy explicit.
- [x] Shorten launch to seven rows with the proposal last and group report to eight concise sections; replace council placeholders with honest pending status and a ready-to-use scoring form.
- [x] Reconcile member reports/TEAM with imported evidence without inventing personal verification.
- [x] Verify frozen inputs, all required files, local links, forbidden term, YAML and numeric consistency; independently review and resolve required findings. Publication follows the final verification and uses the already authorized main push.

## Execution record

- Task 1 complete: 9/9 baseline tests; main cf78f04 and TV4 f9dd0b0 integrated in 8f86b35. TV4 identity and label attribution found in the remote branch; no further user information needed for these.
- Task 2 complete: three E1/CLI tests failed against the original missing implementation, then passed after wiring `tinh_e1`; fourth new test failed for missing two-attempt scoped budget and passed after its implementation. Full suite 13/13; output regenerated.
- Task 3 complete for code/report integration: 14 event definitions, four proposed metrics and four risks; code/YAML budget equal; two independent label columns retained, 18/20 agreement and consensus matches 20/20 reference; four personal reports; local links, table columns, forbidden term/conflict marker scans clean. Independent review: Technical PASS, no required P0–P2 defects; full-course GAPS_FOUND for actual human checks.
- Final review clarification: safety cohorts are locked by intake day and selected chronologically; new requests belong to separate cohorts and do not make older cohorts incomplete. Unknown outcomes/logs still block escalation for the decision cohort. This avoids a never-finished cohort under continuous intake.
- Planning decision: scope-specific pilot budget must include 90 manual cases inside scope and 218 excluded cases; company request denominator matches fixed-cost volume. Original three-attempt A4 remains clearly labeled for rubric comparison.
- Planning decision: each rollout stage provisionally lasts two weeks so mature safety cohorts can exist before escalation; last intake 2027-01-10, mature after 2027-01-18 and decision 2027-01-20. Dates remain proposals; missing evidence means no expansion.
- Council scoring and LMS submission remain actual human actions; the task will report those gaps instead of claiming full course acceptance.
