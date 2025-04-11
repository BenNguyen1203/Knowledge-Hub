**Paper Link:** `https://doi.org/10.48550/arXiv.2002.05810`

**Take home message:** 
Author proposed an end-to-end deep learning model to directly predict the RNA base-pairing matrix, and used an unrolled algorithm for constrained programming as the template for deep architectures to enforce constraints.

E2E deep model combines a *Deep Score Network* with a *Post-Processing Network* based on an unrolled algorithm for solving a constrained optimization problem.

End-to-End Training Algorithm: The training procedure of E2Efold is similar to standard gradient-based supervised learning. However, for RNA secondary structure prediction problems, commonly used metrics for evaluating predictive performances are F1 score, precision and recall, which are non-differentiable.

Comprehensive experiments are conducted to show the superior performance of E2Efold, no matter on quantitative criteria, running time, or visualization.