from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

data_ = {}

etaje_put_args = reqparse.RequestParser()

etaje = {
"parter": {
    "amfiteatre": ["A02", "A03", "AM"],
    "laboratoare": ["002", "003", "FLab004", "005", "030", "031", "032", "043b", "045C",
        "050A", "S07", "FLab008", "FLab007", "FLab006"],
    "seminare": ["027", "028", "042CRU", "043c", "F020", "F19", "F11", "F10"],
    "secretariate": ["029", "041", "045D"],
    "birouri": ["A01", "001", "008A", "008B", "008c", "011", "037", "038", "051B", "051C",
        "054", "055", "056", "057", "058", "059", "061", "062"]},
 "etajul1": {
    "amfiteatre": ["A12", "A13", "139"],
    "laboratoare": ["137", "FLab118", "FLab111", "FLab107", "FLab104", "FLab103", "FLab101B"],
    "seminare": ["103", "104", "105", "106", "107", "108", "128", "130", "132",
        "134", "136", "F108", "F102"],
    "secretariate": ["118"],
    "birouri": ["A11", "101", "102", "127", "138", "141", "144", "148", "149",
        "150", "150A", "152A", "152B", "153A", "153B", "153C", "155A1", "155A2",
         "155A3", "155B", "155C", "151", "153", "154", "156", "158", "159", "160",
          "161", "162", "163", "164", "165", "166", "167", "168", "169", "170",
           "171", "172", "173", "174", "175", "176", "180", "180a", "181"]},
 "etajul2": {
    "amfiteatre": ["AF206"],
    "laboratoare": ["FLab204", "FLab202", "FLab202B"],
    "seminare": ["201", "202", "203", "204", "205", "206", "207", "208", "223", "F203", "F207"],
    "secretariate": ["225", "226", "228", "229", "230", "235", "236", "237", "238", "239",
        "240", "241", "242", "243", "244"],
    "birouri": ["212", "227", "247", "F205"]},
 "etajul3": {
    "amfiteatre": ["A31", "A32", "A33"],
    "seminare": ["301", "302", "303", "304", "305", "306", "307", "308",
        "326", "327", "328", "329", "330", "334"],
    "laboratoare": ["314a", "314b"]},
 "etajul4": {
    "laboratoare": ["402", "405", "406", "408", "409", "410", "411", "412", "413", "414"],
    "seminare": ["424", "423", "422", "421", "420", "419", "418", "416", "415"]},
 "etajul5": {
    "seminare": ["501", "521", "522", "523"],
    "secretariate": ["510", "511", "512", "513"],
    "birouri": ["502"]},
 "etajul6": {
    "seminare": ["601", "607A", "607B"],
    "secretariate": ["605A1"],
    "birouri": ["605B"]},
 "etajul7": {
    "seminare": ["704A", "704B", "704E"],
    "birouri": ["701", "702", "703", "706"]}
}

class Etaj(Resource):
    def get(self, nr_etaj, sala):

        print(nr_etaj, sala)

        if sala == "0":
            return etaje[nr_etaj]

        if sala in etaje[nr_etaj]["amfiteatre"]:
            return "amfiteatru"
        elif sala in etaje[nr_etaj]["laboratoare"]:
            return "laborator"
        elif sala in etaje[nr_etaj]["seminare"]:
            return "seminar"
        elif sala in etaje[nr_etaj]["secretariate"]:
            return "secretariat"
        elif sala in etaje[nr_etaj]["birouri"]:
            return "birou"


        # return etaje[nr_etaj]


api.add_resource(Etaj, "/etaj/<string:nr_etaj>/<string:sala>")

if __name__ == '__main__':
    app.run(debug = False, host='0.0.0.0')
