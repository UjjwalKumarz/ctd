
PROMPTS = {
    "Section 2.7.3.1" : {
        "title": "2.7.3.1 Background and Overview of Clinical Efficacy",
        "template" : f"""I want you to create an specific section i.e. Section 2.7.3.1 of the drug efficacy report for the given drug in **html**. 
            The detailed information about the required section is given below.

            ###############################################
            Details:\n
            Section 2.7.3.1 Background and Overview of Clinical Efficacy \n 
            This section should describe the program of controlled studies and other pertinent studies in the application that evaluated efficacy
            specific to the indication(s) sought. Any results of these studies that are pertinent to evaluation of safety should be discussed 
            in Section 2.7.4, Summary of Clinical Safety. \n The section should begin with a brief overview of the design of the controlled studies 
            that were conducted to evaluate efficacy. These studies include dose-response, comparative efficacy, long-term efficacy, and efficacy 
            studies in population subsets. Critical features of study design should be discussed, e.g., randomisation, blinding, choices of control 
            treatment, choice of patient population, unusual design features such as crossover or randomised withdrawal designs, use of run-in 
            periods, other methods of “enrichment”, study endpoints, study duration, and prespecified plans for analysis of the study results. 
            Although this section is intended to focus on clinical investigations, nonclinical data and clinical pharmacology data may also be 
            referenced as appropriate to provide a comprehensive summary of human experience related to efficacy. This section should not include 
            detailed information about individual studies.

            Subparts: 
            {[
                'Introduction', 
                'Overview of Controlled Studies', 
                'Critical Features of Study Design',
                'Inclusion of Nonclinical and Clinical Pharmacology Data',
                'Exclusion of Detailed Information about Individual Studies',
                'References'
            ]}
            ###############################################

            Your task is to analyse the given detailed information, and **all the possible subparts** that needs to be present in the Section 2.7.3.1.
            At first provide all the steps and information that needs to be present in each sub-part. Kindly elaborate everything that needs to be present in each of the subpart only in the text format. 
            Also do not write text like- now, I will generate HTML for subparts or any text similar to this.
            
            After the above task user will ask you to generate each of the subparts with effective queries. You will have to generate the html body of the subpart first and then fill 
            all the generated content in the body.""",
        "subparts" : [
            'Introduction', 
            'Overview of Controlled Studies', 
            'Critical Features of Study Design',
            'Inclusion of Nonclinical and Clinical Pharmacology Data',
            'Exclusion of Detailed Information about Individual Studies',
            'References'
        ]
    },
    "Section 2.7.3.2" : {
        "title": "2.7.3.2 Summary of Results of Individual Studies",
        "template" : f"""I want you to create an specific section i.e. Section 2.7.3.2 of the drug efficacy report for the given drug in **html**. 
            The detailed information about the required section is given below.

            ###############################################
            Details:\n
            Section 2.7.3.2 Summary of Results of Individual Studies\n
            A tabular listing of all studies that provided (or were designed to provide) information relevant to product efficacy should 
            generally be provided (see the section 2.7.3.6 Appendix), together with narrative descriptions for important studies. 
            The narrative descriptions should be brief, e.g., similar to an abstract for a journal article, and should describe critical design 
            features and critical results. Similar studies may be described together, noting the individual study results and any important 
            differences among the studies. For studies that also contributed significantly to the safety analysis, study narratives should 
            include information about the extent of exposure of study subjects to the test drug or control agent, and how safety 
            data were collected. These narratives can be abstracted from the synopses of the clinical study reports (ICH E3). References or 
            electronic links to the full report of each study should be included in the narratives.
            Narratives of any bridging studies using  clinical endpoints, i.e., certain studies intended to evaluate the ability to extrapolate 
            certain types of foreign clinical data to the new region (see ICH E5), should be included in this section. An analysis of the results 
            of such studies, together with other information (e.g., PK and PD data) that addresses the ability to extrapolate the efficacy and 
            safety results of foreign studies, should be performed if necessary. The conclusions of such an analysis should be noted at the start 
            of Section 2.7.3.3.2, Comparison of Efficacy Results of All Studies, and the full report of the analysis should be provided in Module 5.

            Subparts:
            {[
            'Tabular Listing of Studies',
            'Narrative Descriptions for Important Studies',
            'Bridging Studies',
            'Safety Data Collection in Efficacy Studies',
            'References and Links to Full Study Reports'
            ]}
            ###############################################

            Your task is to analyse the given detailed information, and **all the possible subparts** that needs to be present in the Section 2.7.3.2.
            At first provide all the steps and information that needs to be present in each sub-part. Kindly elaborate everything that needs to be present in each of the subpart only in the text format. 
            Also do not write text like- now, I will generate HTML for subparts or any text similar to this.
            
            After the above task user will ask you to generate each of the subparts with effective queries. You will have to generate the html body of the subpart first and then fill 
            all the generated content in the body.""",
        "subparts" : [
            'Tabular Listing of Studies',
            'Narrative Descriptions for Important Studies',
            'Bridging Studies',
            'Safety Data Collection in Efficacy Studies',
            'References and Links to Full Study Reports'
        ]
    },
    "Section 2.7.3.3" : {
        "template" : """I have to create an specific section i.e. Section 2.7.3.3 of the drug efficacy report for the given drug. I want your
            help to do this. Below is the detailed information about the required section.

            ###############################################
            Details:\n
            2.7.3.3 Comparison and Analyses of Results Across Studies
            Using text, figures, and tables as appropriate (see section 2.7.3.6 Appendix), the subsections of 2.7.3.3 should summarize all 
            available data that characterize the efficacy of the drug. This summary should include analyses of all data, irrespective of their 
            support for the overall conclusion and should, therefore, discuss the extent to which the results of the relevant studies do or do 
            not reinforce each other. Any major inconsistencies in the data regarding efficacy should be addressed, and any areas needing 
            further exploration should be identified.

            The section will generally use two kinds of analyses: comparison of results of individual studies and analysis of data combined 
            from various studies. Details of analyses that are too extensive to be reported in a summary document should be presented in a 
            separate report to be placed in Module 5, section 5.3.5.3.
            
            This section should also cross-reference important evidence from section 2.7.2, such as data that support the dosage and administration 
            section of the labeling. These data include dosage and dose interval recommended, evidence pertinent to individualization of dosage and 
            need for modifications of dosage for specific subgroups (e.g., pediatric or geriatric subjects, subjects with hepatic or renal impairment), 
            and data relevant to dose-response or concentration response (PK/PD) relationships.
            ###############################################

            Your task is to analyse the given detail and find out **all the possible sub-parts** that needs to be present in the Section 2.7.3.3.
            Also provide all the steps and information that needs to be present in each sub-part. Kindly elaborate everything.""",
        "subparts" : {}
    },
    "Section 2.7.3.4" : {
        "template" : """I have to create an specific section i.e. Section 2.7.3.4 of the drug efficacy report for the given drug. I want your
            help to do this. Below is the detailed information about the required section.

            ###############################################
            Details:\n
            2.7.3.4 Analysis of Clinical Information Relevant to Dosing Recommendations
            This section should provide an integrated summary and analysis of all data that pertain to the dose-response or blood level-response 
            relationships of effectiveness (including dose-blood level relationships) and thus have contributed to dose selection and choice of 
            dose interval. Relevant data from nonclinical studies may be referenced, and relevant data from pharmacokinetic studies, other clinical 
            pharmacology studies, and controlled and uncontrolled clinical studies should be summarized to illustrate these dose-response or blood 
            level-response relationships. For PK and PD studies from which data have been summarized in section 2.7.2.2, it may be appropriate to 
            draw on those data in this summary while cross-referencing the summaries in section 2.7.2.2, without repeating those summaries.

            While the interpretation of how these data support specific dosing recommendations should be supplied in the Clinical Overview document, 
            the individual study results and any cross-study analyses that will be used to support the dosing recommendations (including the 
            recommended starting and maximal doses, the method of dose titration, and any other instructions regarding individualization of dosage) 
            should be summarized here. Any identified deviations from relatively simple dose-response or blood level-response relationships due to 
            nonlinearity of pharmacokinetics, delayed effects, tolerance, or enzyme induction should be described.

            Any evidence of differences in dose-response relationships that result from a patient’s age, sex, race, disease, or other factors should 
            be described. Any evidence of different PK or PD responses should also be discussed, or discussions in section 2.7.2 can be cross-referenced. 
            The ways in which such differences were looked for, even if no differences were found, should be described (e.g., specific studies in 
            subpopulations, analysis of efficacy results by subgroup, or blood level determinations of the test drug).
            ###############################################

            Your task is to analyse the given detail and find out **all the possible sub-parts** that needs to be present in the Section 2.7.3.4.
            Also provide all the steps and information that needs to be present in each sub-part. Kindly elaborate everything.""",
        "subparts" : {}
    },
    "Section 5.3.1" : {
        "template" : """I have to create an specific section i.e. Section 5.3.1 of the drug efficacy report for the given drug. I want your
            help to do this. Below is the detailed information about the required section.

            ###############################################
            Details:\n
            5.3.1 Reports of Biopharmaceutic Studies
            BA studies evaluate the rate and extent of release of the active substance from the medicinal product. Comparative BA or BE studies may use PK, PD, clinical, or in vitro dissolution endpoints, and may be either single dose or multiple dose. When the primary purpose of a study is to assess the PK of a drug, but also includes BA information, the study report should be submitted in section 5.3.1, and referenced in sections 5.3.1.1 and/or 5.3.1.2.
            5.3.1.1 Bioavailability (BA) Study Reports
            Contains Nonbinding Recommendations
            58
            BA studies in this section should include:
            • Studies comparing the release and systemic availability of a drug substance from a solid oral dosage form to the systemic availability of the drug substance given intravenously or as an oral liquid dosage form
            • Dosage form proportionality studies
            • Food-effect studies
            5.3.1.2 Comparative BA and Bioequivalence (BE) Study Reports
            Studies in this section compare the rate and extent of release of the drug substance from similar drug products (e.g., tablet to tablet, tablet to capsule). Comparative BA or BE studies may include comparisons between:
            • The drug product used in clinical studies supporting effectiveness and the to-be-marketed drug product
            • The drug product used in clinical studies supporting effectiveness and the drug product used in stability batches
            • Similar drug products from different manufacturers
            5.3.1.3 In Vitro - In Vivo Correlation Study Reports
            In vitro dissolution studies that provide BA information, including studies used in seeking to correlate in vitro data with in vivo correlations, should be placed in section 5.3.1.3. Reports of in vitro dissolution tests used for batch quality control and/or batch release should be placed in the Quality section of the CTD.
            5.3.1.4 Reports of Bioanalytical and Analytical Methods for Human Studies
            Bioanalytical and/or analytical methods for biopharmaceutic studies or in vitro dissolution studies should ordinarily be provided in individual study reports. Where a method is used in multiple studies, the method and its validation should be included once in section 5.3.1.4 and referenced in the appropriate individual study reports.
            ###############################################

            Your task is to analyse the given detail and find out **all the possible sub-parts** that needs to be present in the Section 5.3.1.
            Also provide all the steps and information that needs to be present in each sub-part. Kindly elaborate everything.""",
        "subparts" : {}
    },
    "Section 5.3.2" : {
        "template" : """I have to create an specific section i.e. Section 5.3.2 of the drug efficacy report for the given drug. I want your
            help to do this. Below is the detailed information about the required section.

            ###############################################
            Details:\n
            5.3.2 Reports of Studies Pertinent to Pharmacokinetics Using Human Biomaterials
            Human biomaterials is a term used to refer to proteins, cells, tissues and related materials derived from human sources that are used in 
            vitro or ex vivo to assess PK properties of drug substances. Examples include cultured human colonic cells that are used to assess permeability 
            through biological membranes and transport processes and human albumin that is used to assess plasma protein binding. Of particular importance 
            is the use of human biomaterials such as hepatocytes and/or hepatic microsomes to study metabolic pathways and to assess drug-drug 
            interactions with these pathways. Studies using biomaterials to address other properties (e.g., sterility or pharmacodynamics) should not be placed in the Clinical Study Reports section, but in the Nonclinical Study section (Module 4).
            5.3.2.1 Plasma Protein Binding Study Reports
            Ex vivo protein binding study reports should be provided here. Protein binding data from PK blood and/or plasma studies should be provided in section 5.3.3.
            5.3.2.2 Reports of Hepatic Metabolism and Drug Interaction Studies
            Reports of hepatic metabolism and metabolic drug interaction studies with hepatic tissue should be placed here.
            5.3.2.3 Reports of Studies Using Other Human Biomaterials
            Reports of studies with other biomaterials should be placed in this section.
            ###############################################

            Your task is to analyse the given detail and find out **all the possible sub-parts** that needs to be present in the Section 5.3.2.
            Also provide all the steps and information that needs to be present in each sub-part. Kindly elaborate everything.""",
        "subparts" : {}
    },
    "Section 5.3.3" : {
        "template" : """""",
        "subparts" : {}
    }
}


modules = {
    "Section 2" : {
        "Section 2.6" : {
            "Section 2.6.2" : {
                "Section 2.6.2.1" : [],
                "Section 2.6.2.2" : [],
                "Section 2.6.2.3" : []
            }
        },
        "Section 2.7" : {
            "Section 2.7.3" : {
                "Section 2.7.3.1" : [],
                "Section 2.7.3.2" : [],
                "Section 2.7.3.3" : []
            },
            "Section 2.7.4" : {
                "Section 2.7.4.2" : []
            }
        }
    },
    "Section 5": {
        "Section 5.3" : {
            "Section 5.3.1" : {},
            "Section 5.3.2" : {},
            "Section 5.3.3" : {}
        },
        "Section 5.4" : []
    }
}

