from dataclasses import dataclass

template = open("template.html", "r").read()
print(template)


@dataclass
class Paper:
    title: str
    authors: [str]
    journal: str
    year: str
    link: str

papers = [
    Paper(
		"Response of Lanthanide Sesquioxides to High-Energy Ball Milling",
		["Eric C O'Quinn",  "Alexandre P Solomon", "Casey Corbridge", "Cale Overstreet", "Cameron Tracy", "Antonio F Fuentes", "David J Sprouster", "Maik K Lang"],
		"Advanced Engineering Materials",
		"2025",
		"https://advanced.onlinelibrary.wiley.com/doi/pdfdirect/10.1002/adem.202401251"
    ),
    Paper(
		"Structural stability of REE-PO<sub>4</sub> (REE=Sm,Tb) under swift heavy ion irradiation",
		["Cale Overstreet", "Jacob Cooper", "Eric O'Quinn", "William Cureton", "Raul Palomares", "Julia Leys", "Guido Deissmann", "Stefan Neumeier", "Chien-Hung Chen", "Maik Lang"],
		"Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms",
		"2022",
		"https://www.sciencedirect.com/science/article/pii/S0168583X22001884",
    ),
    Paper(
		"Comparison of short-range order in irradiated dysprosium titanates",
		["Roman Sherrod", "Eric C O'Quinn", "Igor M Gussev", "Cale Overstreet", "Joerg Neuefeind", "Maik K Lang"],
		"npj Materials Degradation",
		"2021",
		"https://www.nature.com/articles/s41529-021-00165-6"
    ),
    Paper(
		"Systematic study of short-and long-range correlations in RE<sub>3</sub>TaO<sub>7</sub> weberite-type compounds by neutron total scattering and X-ray diffraction",
		["Igor M Gussev", "Eric C O'Quinn", "Matthew Tucker", "Rodney C Ewing", "Cale Overstreet", "Joerg Neuefeind", "Michelle Everett", "Qiang Zhang", "David Sprouster", "Daniel Olds", "Gianguido Baldinozzi", "Maik Lang"],
		"Journal of Materials Chemistry A",
		"2023",
		"https://www.nature.com/articles/s41529-021-00165-6"
    ),
    Paper(
		"Swift heavy ion irradiation effects in zirconium and hafnium carbides",
		["Evan Williams", "Jacob Minnette", "Eric O'Quinn", "Alexandre Solomon", "Cale Overstreet", "William F Cureton", "Ina Schubert", "Christina Trautman", "Changyong Park", "Maxim Zdorovets", "Maik Lang"],
		"Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms",
		"2024",
		"https://www.sciencedirect.com/science/article/pii/S0168583X2400017X"
    )
]

@dataclass
class Presentation:
    title: str
    date: str
    conference: str
    location: str

presentations = [
    Presentation(
		"Characterizing swift heavy ion-induced amorphous phases in complex oxides",
		"2023-09-05",
		"Conference on Radiation Effects in Insulators 21",
		"Fukuoka, Japan"
    ),
    Presentation(
			"Structural Stability of REE-PO<sub>4</sub> (REE=Sm,Tb) under Swift Heavy Ion Irradiation",
			"2023-10-02",
			"Materials Science & Technology 23",
			"Columbus, Ohio"
    ),
    Presentation(
		"Magnetic Properties of Non-Crystalline Ho<sub>2</sub>Ti<sub>2</sub>O<sub>7</sub> Pyrochlore Prepared by Far-From-Equilibrium Processing",
		"2024-10-05",
		"Materials Science & Technology 24",
		"Pittsburgh, Pennsylvania"
    )
]


def generate_papers_html(papers):
    out = ""

    for n_paper, p in enumerate(papers):
        author_str = ""
        for i, a in enumerate(p.authors):
            print(i, a, len(p.authors), i == len(p.authors) - 1)
            if "Cale" in a:
                author_str += f"""<span style="font-weight: bold;">{a}</span>, """
            elif i == len(p.authors) - 1:
                author_str += a
            else:
                author_str += a + ", "


        frag = f"""
            <div style="padding: 0.5rem; display: flex; flex-direction: column; gap: 0.5rem">
                <a href="{p.link}"><p>{p.title} (<span style="font-weight: bold;">{p.year}</span>)</p></a>
                <p style="font-style: italic">{p.journal}</p>
                <p>
                    {author_str}  
                </p>
            </div>
        """

        if n_paper == len(papers) - 1:
            pass
        else:
            frag += "<hr>"

        out += frag

    return out

def generate_presentations_html(presentations):
    out = ""
    for i, p in enumerate(presentations):

        frag = f"""
            <div style="padding: 0.5rem; display: flex; flex-direction: column; gap: 0.5rem">
                <p style="font-style: italic">{p.title}</p>
                <p>{p.date}</p>
                <p>{p.conference}</p>
                <p>{p.location}</p>
            </div>
        """

        if i == len(presentations) - 1:
            pass
        else:
            frag += "<hr>"


        out += frag

    return out


filled = template\
    .replace("$PAPERS", generate_papers_html(papers))\
    .replace("$PRESENTATIONS", generate_presentations_html(presentations))

with open("html/index.html", "w") as f:
    f.write(filled)
