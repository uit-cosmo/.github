import matplotlib.pyplot as plt
import model.point_model as pm
import cosmoplots

axes_size = cosmoplots.set_rcparams_dynamo(plt.rcParams, num_cols=1, ls="thin")

model = pm.PointModel(gamma=0.5, total_duration=100, dt=0.01)
times, signal = model.make_realization()

plt.plot(times, signal)
plt.xlabel(r'$t$')
plt.ylabel(r'$\Phi_k(t)$')
plt.savefig('fpp.png', bbox_inches="tight")
plt.show()
