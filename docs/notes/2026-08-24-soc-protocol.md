\# MSTAR SOC Protocol Notes



\- \*\*Standard Operating Condition (SOC)\*\*: Standard benchmark for MSTAR vehicle classification.

\- \*\*Depression Angles\*\*: Train on 17° elevation angle, test on 15° elevation angle.

\- \*\*Why it prevents leakage\*\*: Splitting strictly by physical acquisition angle ensures the model learns true target geometry rather than overfitting to specific viewing conditions or memorizing adjacent frames.

\- \*\*Evaluation Target\*\*: Verifies model generalization across slight angular variations in radar backscatter.

