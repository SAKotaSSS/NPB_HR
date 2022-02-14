import pandas as pd

npb = pd.read_csv("csvfiles/npb_h.csv")

dr_npb = ["選手名", "チーム", "盗塁", "本塁打"]
npb_t = npb.drop(dr_npb, axis=1)
npb_hr = npb.loc[range(0, 289), "本塁打"]

npb_t.to_csv("npb_ht.csv", index=False)
npb_hr.to_csv("npb_htr.csv", index=False)
