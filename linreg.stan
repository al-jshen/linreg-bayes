data {
  int<lower=1> N;
  vector[N] x;
  vector[N] y;
}

parameters {
  real alpha;
  real beta;
  real<lower=0> sigma;
}

model {
  # likelihood
  y ~ normal(alpha + beta * x, sigma);

  # priors
  alpha ~ normal(35, 15);
  beta ~ lognormal(0.1, 1);
  sigma ~ uniform(0, 20);
}
