import pandas as pd

da = []

for n in range(21, 16, -1):
    if n == 21:
        url = "https://baseball-data.com//stats/hitter-all/tpa-3.html"
    else:
        url = f"https://baseball-data.com/{n}//stats/hitter-all/tpa-3.html"
    da = pd.read_html(url, header=1)[0]
    np = pd.DataFrame(da)
    np_h = np.drop("順位", axis=1)
    np_h.to_csv(f"npb_h{n}.csv", index=False)

print(np_h)