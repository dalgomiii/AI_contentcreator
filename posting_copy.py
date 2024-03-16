import time
from getCredentials import getCreds, makeApiCall
from postCreator import get_completion_from_messages, get_image_url

from openai import OpenAI
import random

"""
Add your OpenAI api key between the quotes
"""
client = OpenAI(api_key=' ') 

stem_fields = [
    "Aerospace Engineering",
    "Agricultural Science",
    "Algebra",
    "Anatomy",
    "Anthropology",
    "Applied Mathematics",
    "Aquatic Biology",
    "Architecture",
    "Artificial Intelligence",
    "Astrophysics",
    "Atmospheric Science",
    "Automation Engineering",
    "Biochemistry",
    "Bioinformatics",
    "Biomechanics",
    "Biomedical Engineering",
    "Biophysics",
    "Biostatistics",
    "Botany",
    "Cartography",
    "Cell Biology",
    "Chemical Engineering",
    "Chemistry",
    "Civil Engineering",
    "Climate Science",
    "Cognitive Science",
    "Computational Biology",
    "Computational Chemistry",
    "Computational Linguistics",
    "Computer Engineering",
    "Computer Graphics",
    "Computer Science",
    "Conservation Biology",
    "Control Systems Engineering",
    "Cryptography",
    "Data Science",
    "Developmental Biology",
    "Earth Science",
    "Ecology",
    "Electrical Engineering",
    "Energy Engineering",
    "Environmental Engineering",
    "Environmental Science",
    "Epidemiology",
    "Evolutionary Biology",
    "Fluid Mechanics",
    "Forensic Science",
    "Game Theory",
    "Genetics",
    "Geography",
    "Geology",
    "Geophysics",
    "Graph Theory",
    "Human Biology",
    "Hydrology",
    "Industrial Engineering",
    "Information Technology",
    "Inorganic Chemistry",
    "Machine Learning",
    "Marine Biology",
    "Materials Engineering",
    "Mathematics",
    "Mechanical Engineering",
    "Medical Imaging",
    "Microbiology",
    "Molecular Biology",
    "Nanotechnology",
    "Neuroscience",
    "Nuclear Engineering",
    "Nuclear Physics",
    "Number Theory",
    "Oceanography",
    "Operations Research",
    "Optics",
    "Organic Chemistry",
    "Paleontology",
    "Particle Physics",
    "Petroleum Engineering",
    "Pharmacology",
    "Physical Chemistry",
    "Physics",
    "Physiology",
    "Plant Biology",
    "Probability Theory",
    "Process Engineering",
    "Psychology",
    "Quantum Computing",
    "Quantum Mechanics",
    "Robotics",
    "Seismology",
    "Signal Processing",
    "Social Network Analysis",
    "Software Engineering",
    "Statistics",
    "Structural Engineering",
    "Supply Chain Management",
    "Sustainability Science",
    "Systems Biology",
    "Telecommunications Engineering",
    "Theoretical Physics",
    "Thermodynamics",
    "Topology",
    "Toxicology",
    "Transportation Engineering",
    "Urban Planning",
    "Virology",
    "Wildlife Biology",
    "Zoology",
    "Acoustical Engineering",
    "Algebraic Geometry",
    "Analytical Chemistry",
    "Animal Behavior",
    "Applied Physics",
    "Biochemical Engineering",
    "Bioinorganic Chemistry",
    "Biomaterials",
    "Business Intelligence",
    "Cellular Biology",
    "Chemical Biology",
    "Climatology",
    "Cognitive Psychology",
    "Communication Engineering",
    "Complexity Theory",
    "Computational Neuroscience",
    "Computer Vision",
    "Conservation Genetics",
    "Data Mining",
    "Differential Equations",
    "Digital Signal Processing",
    "Earthquake Engineering",
    "Econometrics",
    "Electromagnetism",
    "Energy Physics",
    "Environmental Chemistry",
    "Environmental Economics",
    "Evolutionary Genetics",
    "Experimental Psychology",
    "Finite Element Analysis",
    "Food Science",
    "Functional Analysis",
    "Game Development",
    "Genetic Engineering",
    "Geographical Information Systems (GIS)",
    "Gravitational Physics",
    "Health Informatics",
    "Human Genetics",
    "Industrial Design",
    "Inorganic Materials",
    "Linguistics",
    "Machine Vision",
    "Manufacturing Engineering",
    "Marine Geology",
    "Mathematical Biology",
    "Mathematical Physics",
    "Mathematical Programming",
    "Mechanical Design",
    "Medical Physics",
    "Metallurgy",
    "Microelectronics",
    "Mobile Computing",
    "Molecular Modeling",
    "Music Technology",
    "Nanoengineering",
    "Natural Language Processing",
    "Neurobiology",
    "Nonlinear Dynamics",
    "Nuclear Chemistry",
    "Operations Management",
    "Organic Synthesis",
    "Paleoclimatology",
    "Parallel Computing",
    "Petrology",
    "Pharmaceutical Chemistry",
    "Physical Geography",
    "Plasma Physics",
    "Polymer Chemistry",
    "Population Genetics",
    "Power Systems Engineering",
    "Probability and Statistics",
    "Psychometrics",
    "Quantum Field Theory",
    "Quantum Optics",
    "Quantum Information Science",
    "Remote Sensing",
    "Renewable Energy Engineering",
    "Risk Management",
    "Scientific Computing",
    "Semiconductor Physics",
    "Simulation Modeling",
    "Soil Science",
    "Space Physics",
    "Statistical Genetics",
    "Structural Biology",
    "Superconductivity",
    "Surface Chemistry",
    "Synthetic Biology",
    "Systems Engineering",
    "Textile Engineering",
    "Time Series Analysis",
    "Transportation Planning",
    "Urban Design",
    "User Experience Design (UX Design)",
    "Veterinary Science",
    "Virtual Reality",
    "Water Resources Engineering",
    "Web Development",
    "Wireless Communications",
    "Agricultural Engineering",
    "Algebraic Topology",
    "Analytical Geometry",
    "Animal Physiology",
    "Applied Chemistry",
    "Astrobiology",
    "Atomic Physics",
    "Bayesian Statistics",
    "Behavioral Ecology",
    "Bioacoustics",
    "Bioethics",
    "Biogeochemistry",
    "Biological Anthropology",
    "Biomolecular Engineering",
    "Bioprocess Engineering",
    "Business Analytics",
    "Catastrophe Theory",
    "Chemical Ecology",
    "Civil Infrastructure Engineering",
    "Climatic Modeling",
    "Cognitive Neuroscience",
    "Communication Theory",
    "Computational Linguistics",
    "Computer Animation",
    "Consumer Psychology",
    "Control Theory",
    "Crystallography",
    "Cybernetics",
    "Decision Theory",
    "Digital Marketing",
    "Disaster Management",
    "Dynamic Systems",
    "Ecological Economics",
    "Electric Power Systems",
    "Environmental Geology",
    "Environmental Physics",
    "Enzymology",
    "Financial Mathematics",
    "Fluid Dynamics",
    "Forestry",
    "Game Design",
    "General Relativity",
    "Geographic Information Science",
    "Geochemistry",
    "Health Economics",
    "Human-Computer Interaction",
    "Industrial Ecology",
    "Industrial Microbiology",
    "Inorganic Synthesis",
    "Machine Translation",
    "Marine Ecology",
    "Mathematical Economics",
    "Mechanical Physics",
    "Medical Chemistry",
    "Meteorology",
    "Microbial Genetics",
    "Mobile Robotics",
    "Molecular Genetics",
    "Multimedia Computing",
    "Nanobiotechnology",
    "Natural Resource Economics",
    "Network Theory",
    "Nonlinear Control Systems",
    "Nuclear Magnetic Resonance",
    "Operations Research",
    "Organic Electronics",
    "Paleobiology",
    "Parallel Processing",
    "Petroleum Geology",
    "Pharmaceutical Engineering",
    "Photovoltaics",
    "Plant Ecology",
    "Population Ecology",
    "Process Control",
    "Quantum Chemistry",
    "Radiochemistry",
    "Renewable Energy Systems",
    "Robotics Engineering",
    "Rural Sociology",
    "Software Development",
    "Solid State Physics",
    "Space Science",
    "Speech Recognition",
    "Statistical Physics",
    "Stochastic Processes",
    "Structural Dynamics",
    "Sustainable Development",
    "Systems Analysis",
    "Telemedicine",
    "Theoretical Chemistry",
    "Transportation Systems",
    "Urban Geography",
    "Wildlife Management"
]
hashtags = '#instagood #trending #explorepage #viral #followme #picoftheday #follow #instadaily #trendingnow #instalike #viralpost #igers #instagram #motivation #meme #lol #cool #insta #science #knowledge #physics #computerscience #chemistry #mathematics #cs'

subject = stem_fields[random.randint(0,len(stem_fields)-1)]

messages = [

    {'role':'system', 'content': f"You are an Instagram content creator who likes {subject} \ You understand concepts in these fields at a university or post-graduate research level and can explain to others at the level of a high school student \ You will generate 1 Instagram Post about any concept from {subject} and explain it like how you would explain it to a high school student. \ Each pointer will start with an emoji. \ You do this by citing relavant works by the scientists and include the year it was released; and explain how they are relavent to said topic.\ You will also include examples of how this concept is employed in everyday life. \ At the end, I want to ask a question about the topic that invokes discussion of said topic."},

    {'role':'user','content': f'Create Instagram content and spread knowledge about complex {subject} concepts of university level with hashtags'}

]


caption = get_completion_from_messages(client,input_message=messages , temperature=0.5).replace("**", "")

image_prompter = [

    {'role':'system', 'content': f"You are someone in the STEM fields who knows a lot about scientists in the field of {subject} \ You know who they are, what they do, what are their works and how their works are important. \ You can identify names of scientists from a text."},

    {'role':'user','content': f'From this text "{caption}", I want to find out who the scientist(s) and write me a description of a situation of them at work / research. \ If there are no scientists, write me a description of an illustration describing {subject} / The description of the image should be in line with the image generation rules of OpenAI / I want the image to look cartoonish'}
]
image_prompt = get_completion_from_messages(client,input_message=image_prompter , temperature=0)


def createMediaObject(params):

    url = params['endpoint_base']+params['instagram_account_id'] + '/media'

    endpointParams = dict()
    endpointParams['caption'] = params['caption']
    endpointParams['access_token']=params['access_token']

    if 'IMAGE' == params['media_type']:
        endpointParams['image_url'] = params["media_url"]
    else:
        endpointParams['video_url'] = params['media_url']
        endpointParams['media_type'] = params['media_type']

    return makeApiCall(url,endpointParams,'POST')

def getMediaObjectStatus( mediaObjectId, params ) :
	url = params['endpoint_base'] + '/' + mediaObjectId # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'status_code' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return makeApiCall( url, endpointParams, 'GET' ) # make the api call

def publishMedia( mediaObjectId, params ) :
      
	url = params['endpoint_base'] + params['instagram_account_id'] + '/media_publish' # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['creation_id'] = mediaObjectId # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return makeApiCall( url, endpointParams, 'POST' ) # make the api call


params = getCreds()
params['media_type'] = 'IMAGE'
params['media_url'] = get_image_url(client,image_prompt)
params['caption'] = caption + hashtags

imageMediaObjectResponse = createMediaObject (params)
imageMediaObjectId = imageMediaObjectResponse['json_data']['id']
imageMediaStatusCode = 'IN_PROGRESS'

print("\n ---- IMAGE MEDIA OBJECT ---- \n")
print("\tID:")
print("\t"+imageMediaObjectId)

while imageMediaStatusCode != 'FINISHED' : # keep checking until the object status is finished
	imageMediaObjectStatusResponse = getMediaObjectStatus( imageMediaObjectId, params ) # check the status on the object
	imageMediaStatusCode = imageMediaObjectStatusResponse['json_data']['status_code'] # update status code

	print( "\n---- IMAGE MEDIA OBJECT STATUS -----\n" ) # display status response
	print( "\tStatus Code:" ) # label
	print( "\t" + imageMediaStatusCode ) # status code of the object

	time.sleep( 5 ) # wait 5 seconds if the media object is still being processed

publishImageResponse = publishMedia( imageMediaObjectId, params ) # publish the post to instagram