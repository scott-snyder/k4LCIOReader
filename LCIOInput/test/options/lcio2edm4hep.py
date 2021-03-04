#!/usr/bin/env python

from Gaudi.Configuration import *

from Configurables import k4DataSvc
dsvc = k4DataSvc("EventDataSvc")

# read LCIO files
from Configurables import LCIOInput
read = LCIOInput("read")
read.inputs = [
#"/cefs/data/FullSim/CEPC240/CEPC_v4/higgs/smart_final_states/E240.Pffh_invi.e0.p0.whizard195//ffh_inv.e0.p0.00001_1000_sim.slcio"
"/cefs/data/RecData/CEPC250/CEPC_v1/higgs/E250.Pnnh.whizard195/E250-CDR_ws.Pnnh.eU.pU.01232_rec.slcio"
]
read.collections = [
        "SimTrackerHit:COILCollection",
        "SimCalorimeterHit:EcalBarrelSiliconCollection",
        "MCParticle:MCParticle",
        "SimTrackerHit:TPCCollection",
        "SimTrackerHit:VXDCollection",
        "Cluster:ArborCharged",
        "Cluster:ArborNeutral",
        "ReconstructedParticle:ArborChargedCore",
        "ReconstructedParticle:ArborNeutralCore",
        "MCRecoParticleAssociation:RecoMCTruthLink"
        ]

# write PODIO file
from Configurables import PodioOutput
write = PodioOutput("write")
write.filename = "test.root"
write.outputCommands = ["keep *"]

# ApplicationMgr
from Configurables import ApplicationMgr
ApplicationMgr(
        TopAlg = [read, write],
        EvtSel = 'NONE',
        EvtMax = 10,
        ExtSvc = [dsvc],
        OutputLevel=INFO
)
