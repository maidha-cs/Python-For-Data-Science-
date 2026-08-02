risk_levels = ["Low", "High", "Low", "Low", "High"]
# Label_Encoding hum us liya kartaa hein ku ka Machine Learning mein har chez numbers mein hoti hai us liyaa ya text ko
# number mein chg karaa ga
Text_Chg = [ 0 if x == 'Low' else 1 for x in risk_levels]
print(Text_Chg)
