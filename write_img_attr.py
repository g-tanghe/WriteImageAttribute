import sys

"""
Goal:
<img	class="profile_pic"
src="res/profile_pic/2017-2018/Arnaud_Lagast_2017-2018_720.jpg"
srcset="res/profile_pic/2017-2018/Arnaud_Lagast_2017-2018_1152.jpg 1152w,
res/profile_pic/2017-2018/Arnaud_Lagast_2017-2018_1080.jpg 1080w,
res/profile_pic/2017-2018/Arnaud_Lagast_2017-2018_720.jpg 720w"
sizes="	(min-width: 1280px) calc(.25*1216px - 2*8px),
(min-width: 900px) calc(.33*864px - 2*8),
calc(.50*752px - 2*8px)"
alt="Profielfoto van Arnaud Lagast 2017-2018">
"""

# Todo: adjust year
year1 = 2018
year2 = 2019

try:
    file_in = open('in_{}-{}.txt'.format(year1, year2), 'r')
except:
    sys.exit("file_in didn't open correctly!")

try:
    file_out = open('out_{}-{}.txt'.format(year1, year2), 'w')
except:
    sys.exit("file_out didn't open correctly!")

firstname = file_in.readline().strip('\n')
lastname = file_in.readline().strip('\n')
while firstname and lastname:
    lastname_format = lastname.replace(" ", "_")
    file_out.write('{2} {3}:\n\t\t\t\t\t\t\t<img class=\"profile_pic\"\n\t\t\t\t\t\t\t\tsrc=\"res/profile_pic/{0}-{1}/{2}_{4}_{0}-{1}_720.jpg\"\n\t\t\t\t\t\t\t\tsrcset=\"res/profile_pic/{0}-{1}/{2}_{4}_{0}-{1}_1152.jpg 1152w,\n\t\t\t\t\t\t\t\t\t\tres/profile_pic/{0}-{1}/{2}_{4}_{0}-{1}_1080.jpg 1080w,\n\t\t\t\t\t\t\t\t\t\tres/profile_pic/{0}-{1}/{2}_{4}_{0}-{1}_720.jpg 720w\"\n\t\t\t\t\t\t\t\tsizes=\"\t(min-width: 1280px) calc(.25*1216px - 2*8px),\n\t\t\t\t\t\t\t\t\t\t(min-width: 900px) calc(.33*864px - 2*8),\n\t\t\t\t\t\t\t\t\t\tcalc(.50*752px - 2*8px)\"\n\t\t\t\t\t\t\t\talt=\"Profielfoto van {2} {3} {0} - {1}\">\n\n\n'.format(year1, year2, firstname, lastname, lastname_format))
    firstname = file_in.readline().strip('\n')
    lastname = file_in.readline().strip('\n')

file_in.close()
file_out.close()
