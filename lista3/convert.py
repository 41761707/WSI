
def main():
	array=[[0.23734177215189875, 0.0, 0.7120253164556962, 1.0284810126582278, 21.598101265822788, 3.0063291139240507, 0.23734177215189875, 34.49367088607595, 2.3734177215189876, 36.313291139240505],
[80.64516129032258, 0.0, 3.795066413662239, 2.0872865275142316, 0.18975332068311196, 5.502846299810247, 3.795066413662239, 0.18975332068311196, 2.0872865275142316, 1.7077798861480076],
[0.15479876160990713, 72.91021671826626, 12.538699690402478, 0.15479876160990713, 2.321981424148607, 1.08359133126935, 0.30959752321981426, 6.811145510835913, 2.786377708978328, 0.9287925696594427],
[0.9221311475409836, 0.10245901639344263, 3.483606557377049, 14.446721311475411, 0.0, 19.364754098360656, 0.0, 0.10245901639344263, 60.65573770491803, 0.9221311475409836],
[0.24067388688327318, 0.0, 2.7677496991576414, 0.9626955475330927, 44.28399518652226, 3.6101083032490973, 2.166064981949458, 10.95066185318893, 2.166064981949458, 32.851985559566785],
[0.2583979328165375, 0.12919896640826875, 90.82687338501292, 5.167958656330749, 0.0, 0.2583979328165375, 0.9043927648578811, 1.421188630490956, 0.7751937984496124, 0.2583979328165375],
[3.343023255813953, 0.14534883720930233, 1.308139534883721, 0.436046511627907, 2.3255813953488373, 1.4534883720930232, 89.82558139534885, 0.0, 0.872093023255814, 0.29069767441860467],
[0.0, 0.0, 1.1815252416756177, 0.8592910848549946, 24.919441460794843, 3.1149301825993554, 0.0, 43.71643394199785, 2.3630504833512354, 23.8453276047261],
[0.0, 76.85076380728555, 5.052878965922444, 5.64042303172738, 1.2925969447708578, 1.645123384253819, 0.35252643948296125, 4.112808460634548, 3.055229142185664, 1.9976498237367801],
[3.7490436113236423, 0.1530221882172915, 3.5960214231063508, 53.251721499617446, 0.0, 23.488905891354246, 0.1530221882172915, 0.0, 15.14919663351186, 0.45906656465187456],
[92.27373068432672, 0.0, 0.6622516556291391, 0.22075055187637968, 0.0, 1.7660044150110374, 3.532008830022075, 0.0, 1.3245033112582782, 0.22075055187637968],
[6.382978723404255, 0.6648936170212766, 6.515957446808511, 5.319148936170213, 8.77659574468085, 30.45212765957447, 35.77127659574468, 0.26595744680851063, 5.452127659574469, 0.39893617021276595]]
	for item in array:
		result=""
		for element in item:
			result=result+str(round(element, 2))+"\% & "
		print(result)
if __name__=="__main__":
	main()