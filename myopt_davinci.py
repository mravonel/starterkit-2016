#to run DaVinci:
#lb-run DaVinci/v41r2 gaudirun.py myopt_davinci.py
from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *

# Stream and stripping line we want to use
stream = 'AllStreams'
line = 'D2hhCompleteEventPromptDst2D2RSLine'

# Create an ntuple to capture D*+ decays from the StrippingLine line
dtt = DecayTreeTuple('TupleDstToD0pi_D0ToKpi')
#dtt.Inputs = ['/Event/{0}/Phys/{1}/Particles'.format(stream, line)]
dtt.Inputs = ['/Event/AllStreams/Phys/D2hhCompleteEventPromptDst2D2RSLine/Particles']
dtt.Decay = '[D*(2010)+ -> (D0 -> K- pi+) pi+]CC'

from Configurables import DaVinci

# Configure DaVinci
DaVinci().InputType = 'DST'
DaVinci().TupleFile = 'DVntuple.root'
#DaVinci().PrintFreq = 1000
DaVinci().PrintFreq = 100
DaVinci().DataType = '2012'
DaVinci().Simulation = True
# Only ask for luminosity information when not using simulated data
DaVinci().Lumi = not DaVinci().Simulation
#DaVinci().EvtMax = -1
DaVinci().EvtMax = 300
DaVinci().CondDBtag = 'sim-20130522-1-vc-md100'
DaVinci().DDDBtag = 'dddb-20130929-1'

DaVinci().UserAlgorithms += [dtt]

from GaudiConf import IOHelper

# Use the local input data
IOHelper().inputFiles([
  './00035742_00000002_1.allstreams.dst'
], clear=True)

#IOHelper().inputFiles([
#  './00035742_00000002_1.allstreams.dst',
#  './otherfile.dst'
#], clear=True)

