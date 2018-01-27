import sys

# Goal:
#
# Garben Tanghe:
#   <div class="grid-xs grid-sm-2 grid-md-3 grid-l-4">
#       <div class="profile_pic_container">
#           <img class="profile_pic"
#                src="<?php echo $path; ?>res/profile_pic/2017-2018/Garben_Tanghe.jpg"
#                alt="Moeder Peerdevisscher Profielfoto van Garben Tanghe alias Jones 2017 - 2018">
#           <div class="profile_pic_caption">
#               <p class="centered">PR<br><strong>Garben Tanghe</strong><br>alias Jones</p>
#           </div>
#       </div>
#   </div>

yearXXXX = int(input(
    "Please type the first year of the club year.\nThis means the XXXX in the club year noted as XXXX - YYYY.\nXXXX: "))
yearYYYY = yearXXXX + 1

try:
    file_in = open('in_{}-{}.txt'.format(yearXXXX, yearYYYY), 'r')
except:
    sys.exit('file_in didn\'t open correctly!')

try:
    file_out = open('out_{}-{}.txt'.format(yearXXXX, yearYYYY), 'w')
except:
    sys.exit('file_out didn\'t open correctly!')

firstname = 'Firstname'
lastname = 'Lastname'
function = 'Commilito'
while firstname and lastname:
    print('{0} {1} {2}'.format(firstname, lastname, function))
    lastname_format = lastname.replace(" ", "_")
    file_out.write(
        '{2} {3}:\n'
        '<div class=\"grid-xs grid-sm-2 grid-md-3 grid-l-4\">\n'
        '\t<div class=\"profile_pic_container\">\n'
        '\t\t<img class=\"profile_pic\"\n'
        '\t\t\t src=\"res/profile_pic/{0}-{1}/{2}_{4}.jpg\"\n'
        '\t\t\t alt=\"Moeder Peerdevisscher Profielfoto van {2} {3} {5} {0} - {1}\">\n'
        '\t\t<div class=\"profile_pic_caption\">\n'
        '\t\t\t<p class=\"centered\">{6}<br><strong>{2} {3}</strong></p>\n'
        '\t\t</div>\n'
        '\t</div>\n'
        '</div>\n\n'.format(yearXXXX, yearYYYY, firstname, lastname, lastname_format, function, function.upper()))
    firstname = file_in.readline().strip('\n')
    lastname = file_in.readline().strip('\n')
    function = file_in.readline().strip('\n')
    alias = file_in.readline().strip('\n')
    file_in.readline()

file_in.close()
file_out.close()

sys.exit(0)
