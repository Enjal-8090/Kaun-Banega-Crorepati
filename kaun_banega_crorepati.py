
import random
from outro import outro

question_1="Which planet is known as the Red Planet?\nA. Earth\tB. Mars\nC. Jupiter\tD. Saturn  "
question_2="Which of the following instruments is used in differential leveling?\nA. Theodolite\tB. Dumpy Level\nC. Compass\tD. Planimeter  "
question_3="The primary function of white blood cells is to:\nA. Transport oxygen\tB. Fight infections\nC. Clot blood\tD. Carry nutrients  "
question_4="What is the capital of France?\nA. Berlin\tB. Madrid\nC. Paris\tD. Rome  "
question_5="Which of the following errors is systematic?\nA. Mistake in reading a scale\tB. Parallax error\nC. Instrumental error\tD. Random error  "
question_6="The reference ellipsoid used by WGS 84 is centered at:\nA. Center of the Earth\tB. Surface of the Earth\nC. North Pole\tD. Equator  "
question_7="In which year did the World War II end?\nA. 1945\tB. 1939\nC. 1918\tD. 1965  "
question_8="What is the chemical symbol for Gold?\nA. Au\tB. Ag\nC. Gd\tD. Go  "
question_9="In GPS, what does the acronym 'GPS' stand for?\nA. Global Positioning System\tB. General Positioning Satellite\nC. Geographical Positioning System\tD. Global Planning System  "
question_10="The most commonly used unit of frequency is:\nA. Watt\tB. Decibel\nC. Hertz\tD. Ohm  "
question_11="The most commonly used projection for topographic maps is:\nA. Mercator Projection\tB. Robinson Projection\nC. Transverse Mercator Projection\tD. Lambert Conformal Conic Projection  "
question_12="The UTM coordinate system divides the Earth into how many zones?\nA. 30\tB. 120\nC. 90\tD. 60  "
question_13="Which method is used to measure horizontal angles in surveying?\nA. Theodolite\tB. Leveling instrument\nC. Compass\tD. Total station  "
question_14="The process of determining the position of a point on the Earth's surface using satellite signals is called:\nA. Triangulation\tB. Trilateration\nC. GPS surveying\tD. Photogrammetry  "
question_15="The process of determining latitude and longitude is called:\nA. Leveling\tB. Orientation\nC. Position fixing\tD. Triangulation  "
question_16="Which of the following sensors is active?\nA. Landsat\tB. MODIS\nC. LIDAR\tD. Sentinel-2  "
question_17="Which satellite system is developed by the European Union?\nA. GPS\tB. GLONASS\nC. Galileo\tD. BeiDou  "
question_18="Which satellite system is developed by the United States?\nA. GPS\tB. GLONASS\nC. Galileo\tD. BeiDou  "
question_19="Which satellite system is developed by the Russia?\nA. GPS\tB. GLONASS\nC. Galileo\tD. BeiDou "
question_20="Which satellite system is developed by the China?\nA. GPS\tB. GLONASS\nC. Galileo\tD. BeiDou "
cash_prizes=[1000,2000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]


questions={question_1:'B',question_2:'B',question_3:'B',question_4:'C',question_5:'B',question_6:'A',question_7:'A',question_8:'A',question_9:'A',question_10:'C',question_11:'C',question_12:'D',question_13:'A',question_14:'B',question_15:'C',question_16:'C',question_17:'C',question_18:'A',question_19:'B',question_20:'D'}
question_items=list(questions.items())
random.shuffle(question_items)
suff_data=dict(question_items)
outro()
k=0
for i,j in suff_data.items():
    print(f"{i}")
    while True:
        ans=input("Enter the value:")
        if ans.capitalize() in ['A','B','C','D']:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")

    if ans.capitalize()==j:
        print(f"Correct answer!You won {cash_prizes[k]}\n")
        k+=1
        if k==15:
            break
    else:
        print(f"Wrong answer! The correct answer is {j}.")
        break
            
if k<5:
    print("You won ₹0. Better luck next time!")
elif 5<=k<10:
    print("You won ₹20,000!")
elif 10<=k<15:
    print("You won ₹6,40,000!")
else:
    print("Congratulations! You are the Kaun Banega Crorepati winner and won ₹7,00,00,000!")
