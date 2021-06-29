data {
  int<lower=1> N;
  vector[N] x;
  vector[N] y;
}

parameters {
  real alpha;
  real beta;
  real sigma;
}

model {
  # likelihood
  y ~ normal(alpha + beta * x, sigma);

  # priors
  alpha ~ std_normal();
  beta ~ std_normal();
  sigma ~ std_normal();
}
