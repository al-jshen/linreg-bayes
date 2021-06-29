import daft

# setup
pgm = daft.PGM()

# parameters
pgm.add_node("alpha", r"$\alpha$", 0.5, 2)
pgm.add_node("beta", r"$\beta$", 1.5, 2)
pgm.add_node("sigma", r"$\sigma$", 2.5, 2)

# data
pgm.add_node("x", r"$x_i$", 0, 1, observed=True)
pgm.add_node("mu", r"$\mu_i$", 1, 1)
pgm.add_node("y", r"$y_i$", 2, 1, observed=True)

# edges
pgm.add_edge("alpha", "mu")
pgm.add_edge("beta", "mu")
pgm.add_edge("x", "mu")
pgm.add_edge("mu", "y")
pgm.add_edge("sigma", "y")

# plate
pgm.add_plate([-0.5, 0.5, 3, 1], label=r"$i = 1, \cdots, N$", shift=-0.1)

# render and save
pgm.render()
pgm.savefig("pgm.png", dpi=400)
