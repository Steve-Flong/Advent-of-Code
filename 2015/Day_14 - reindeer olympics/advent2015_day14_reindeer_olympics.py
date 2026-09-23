# "score" added for part 2, the race remains the same

def main():
    time = 0
    reindeer = {}
    with open("advent2015_day14.txt") as input:
        for x in input.readlines():
            i = x.split(" ")
            reindeer[i[0]] = {"speed": int(i[3]),
                              "fly": int(i[6]),
                              "rest": int(i[13]),
                              "start": 0,
                              "score": 0,
                              "stop": int(i[6]),
                              "flying": True,
                              "current_distance": 0}
        while time < 2503:
            time += 1
            for deer in reindeer:
                x = reindeer[deer]
                if not x["flying"]:
                    if x["start"] == time:
                        x["flying"] = True
                        x["stop"] = time + x["fly"]
                        continue

                if x["flying"]:
                    if x["stop"] == time:
                        x["flying"] = False
                        x["current_distance"] += x["speed"]
                        x["start"] = time + x["rest"]
                    else:
                        x["current_distance"] += x["speed"]

            dist = [(reindeer[keys]["current_distance"]) for keys in reindeer]
            for keys in reindeer:
                if reindeer[keys]["current_distance"] == max(dist):
                    reindeer[keys]["score"] += 1

        for keys in reindeer:
            print(keys, reindeer[keys])


if __name__=="__main__":
    main()