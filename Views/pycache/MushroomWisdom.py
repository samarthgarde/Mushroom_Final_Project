import streamlit as st
import base64


def app():

    st.markdown("""
        <div class="text">
        Welcome to the **Mushroom Encyclopedia**! This app is your ultimate guide to the fascinating world of mushrooms. 
        Explore their biology, ecology, uses, and cultural significance. Whether you're a mycologist, a forager, or just curious, 
        there's something here for everyone!
        </div>
    """, unsafe_allow_html=True)
    def set_bg_hack_url():

        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url("https://avi-chavan-96.sirv.com/Mushroom/disc-fungus-8298506_1280.jpg");
                background-size: 100% 100%;
                background-position: center;
                min-height: 100vh; /* Minimum height to cover the full viewport */
                height: auto; /* Adjust height based on content */
            }}
            </style>
            """,
            unsafe_allow_html=True)
    set_bg_hack_url()

    # Section 1: Introduction to Mushrooms
    st.header("🍄 Introduction to Mushrooms")
    st.write("""
    Mushrooms are the fruiting bodies of fungi, primarily from the phyla **Basidiomycota** and **Ascomycota**. 
    Unlike plants, mushrooms are **heterotrophs**, meaning they absorb nutrients from their surroundings through **extracellular digestion**. 
    They are incredibly diverse, with over **14,000 known species** and potentially many more undiscovered.
    """)
    st.write("""
    Mushrooms play vital roles in ecosystems as **decomposers**, **symbionts**, and **pathogens**. They are also valued for their **culinary**, **medicinal**, and **cultural significance**.
    """)


    # Section 2: Biology of Mushrooms
    st.header("Biological Classification")
    st.markdown("""
    - **Kingdom**: Fungi  
    - **Phylum**: Basidiomycota (most mushrooms) or Ascomycota  
    - **Structure**:  
      - **Cap (Pileus)**: The prominent part, varying in shapes, sizes, and colors.  
      - **Gills (Lamellae)**: 🌾  Found underneath the cap, they produce microscopic spores for reproduction.  
      - **Stalk (Stem or Stipe)**:  🌿 Elevates the cap for efficient spore dispersal.  
      - **Mycelium**: The hidden, thread-like network beneath the surface, responsible for nutrient absorption and decomposition.
    """)

    st.header("🧬 Biology of Mushrooms")
    st.write("""
    Mushrooms are made of **hyphae**, thread-like structures that form a network called **mycelium**. 
    The **cell walls** contain **chitin**, making them different from plants.
    """)
    with st.expander("🔬 **Cellular Structure and Composition**"):
        st.write("""
        - **Chitin Cell Walls**: Provide structural support and resistance to microbial breakdown.
        - **Ergosterol**: A sterol in fungal cell membranes, similar to cholesterol in animals.
        - **Septa and Coenocytic Hyphae**: Septate hyphae have cross-walls, while coenocytic hyphae lack them.
        """)
    with st.expander("🌱 **Nutritional Modes**"):
        st.write("""
        - **Saprophytic Fungi**: Decompose dead organic matter (e.g., oyster mushrooms).
        - **Parasitic Fungi**: Extract nutrients from living hosts (e.g., *Cordyceps*).
        - **Mutualistic Fungi**: Form symbiotic relationships with plants (e.g., mycorrhizal fungi).
        """)
    with st.expander("🧪 **Biochemical Properties**"):
        st.write("""
        - **Secondary Metabolites**: Mushrooms produce compounds like **psilocybin** (psychedelic) and **lovastatin** (cholesterol-lowering).
        - **Enzymatic Activity**: Fungi produce enzymes like **laccases** and **cellulases** to break down complex organic molecules.
        """)

    # Section 3: Classification
    st.header("📚 Classification of Mushrooms")
    st.write("""
    Mushrooms belong to the **Fungi** kingdom and are classified based on their reproductive structures.
    """)
    st.markdown("""
    | Phylum           | Reproductive Structure | Example Species               |
    |------------------|------------------------|-------------------------------|
    | Basidiomycota    | Basidia (external spores) | *Agaricus bisporus* (Button Mushroom) |
    | Ascomycota       | Asci (internal spores) | *Morchella esculenta* (Morel) |
    | Zygomycota       | Zygospores (fusion of hyphae) | *Rhizopus stolonifer* (Bread Mold) |
    """)
    st.write("""
    - **Basidiomycota**: Includes most common mushrooms like **button mushrooms** and **shiitake**.
    - **Ascomycota**: Includes **morels** and **truffles**.
    - **Zygomycota**: Includes bread molds and less common mushrooms.
    """)

    # Section 4: Anatomy
    st.header("🔬 Anatomy of a Mushroom")
    st.write("""
    Mushrooms have specialized structures that support spore production and dispersal.
    """)
    with st.expander("🍄 **Key Structures**"):
        st.markdown("""
        - **Cap (Pileus)**: Protects the gills and varies in shape.
        - **Gills (Lamellae)**: Produce and release spores.
        - **Stem (Stipe)**: Supports the cap and elevates spores.
        - **Mycelium**: The underground network of hyphae.
        """)
    with st.expander("🔍 **Spore Production**"):
        st.write("""
        - Spores are produced in the **gills** or **pores** of the mushroom.
        - Spore color is a key identification feature (e.g., white, black, brown).
        """)


# Section 4: Types of Mushrooms
    st.header("Types of Mushrooms")
    with st.expander("1. Edible Mushrooms 🍲"):
        st.markdown("""
        - **White Button Mushroom** (*Agaricus bisporus*): Widely consumed; versatile with a mild flavor.  
        - **Portobello Mushroom**: A mature white button mushroom; has a rich, meaty texture.  
        - **Shiitake** (*Lentinula edodes*): A staple in Asian cuisine with a smoky, umami flavor.  
        - **Oyster Mushroom** (*Pleurotus ostreatus*): Fan-shaped, delicate, and mildly flavored.  
        - **Enoki** (*Flammulina velutipes*): Thin, crunchy, and ideal for soups or stir-fries.  
        - **Chanterelle** (*Cantharellus spp.*): Golden-yellow, with a fruity aroma.  
        - **Porcini** (*Boletus edulis*): A prized Italian delicacy with a nutty, earthy flavor.  
        """)

    with st.expander("2. Medicinal Mushrooms 💊"):
        st.markdown("""
        - **Reishi** (*Ganoderma lucidum*): Known as the "mushroom of immortality"; supports immunity and longevity.  
        - **Cordyceps**: Parasitizes insects; boosts energy and vitality.  
        - **Turkey Tail** (*Trametes versicolor*): Enhances immune function, particularly in cancer therapies.  
        - **Lion’s Mane** (*Hericium erinaceus*): Promotes cognitive health and nerve regeneration.  
        """)

    with st.expander("3. Toxic Mushrooms☠️"):
        st.markdown("""
        - **Death Cap** (*Amanita phalloides*): Causes severe liver damage and is responsible for most mushroom poisonings.  
        - **Destroying Angel** (*Amanita bisporigera*): Extremely toxic and often mistaken for edible varieties.  
        - **Fly Agaric** (*Amanita muscaria*): Hallucinogenic in small doses but toxic in larger amounts.  
        - **False Morels** (*Gyromitra spp.*): Resemble edible morels but contain dangerous toxins.  
        """)

    with st.expander("4. Psychedelic Mushrooms 🌈"):
        st.markdown("""
        - **Psilocybin Mushrooms** (*Psilocybe spp.*): Contain psilocybin, used in research for treating depression, PTSD, and anxiety.  
        """)
# Section 5: Nutritional and Health Benefits
    st.header("Nutritional and Health Benefits💪")
    st.markdown("""
    - **Low in Calories**: Perfect for weight management.  
    - **Rich in Nutrients**:  
      - **Proteins**: Include all nine essential amino acids, making them an excellent vegetarian option.  
      - **Vitamins**: High in B-complex vitamins and a rare natural source of vitamin D.  
      - **Minerals**: Contain selenium, potassium, copper, and zinc.  
      - **Dietary Fiber**: Promotes gut health.  
    - **Antioxidants**:  
      - **Ergothioneine**: Reduces oxidative stress.  
      - **Glutathione**: Protects cells from damage.  
    - **Immune-Boosting**:  
      - Polysaccharides like beta-glucans enhance immunity.  
    """)

# Section 6: Ecological Importance
    st.header("🌿 Ecological Importance")
    st.markdown("""
    - **Decomposition**: Break down organic material, enriching the soil and recycling nutrients.  
    - **Symbiosis**:  
      - **Mycorrhizal Fungi**: Form partnerships with plant roots, enhancing nutrient absorption.  
      - **Truffle Symbiosis**: Grow in association with tree roots, aiding plant health.  
    - **Habitat Creation**: Provide food and shelter for many organisms.  
    - **Bioremediation**:  
      - Break down pollutants like oil spills and plastics.  
      - Absorb heavy metals from contaminated soil.
    """)
 #Section 7:Reproduction & Spore Dispersal
    st.header("🌱 Reproduction & Spore Dispersal")
    st.write("""
    Mushrooms reproduce using spores, which can spread through **wind, water, and animals**.
    """)
    with st.expander("🌬️ **Spore Dispersal Mechanisms**"):
        st.markdown("""
        - **Wind**: Spores are lightweight and carried by air currents.
        - **Water**: Spores float on water surfaces.
        - **Animals**: Spores attach to animals or are ingested and dispersed.
        """)
    with st.expander("🔄 **Life Cycle**"):
        st.write("""
        1. **Spore Germination**: Spores land on a suitable substrate and germinate into mycelium.
        2. **Mycelial Growth**: The mycelium spreads and absorbs nutrients.
        3. **Fruiting Body Formation**: Under the right conditions, the mycelium forms a mushroom.
        4. **Spore Release**: The mushroom releases spores to continue the cycle.
        """)

    # Section 8:Evolution & Fossil Record
    st.header("🦕 Evolution & Fossil Record")
    st.write("""
    Fungi evolved over **400 million years ago**, with early fossils like **Prototaxites** (giant prehistoric fungi).
    """)
    with st.expander("📜 **Key Evolutionary Milestones**"):
        st.markdown("""
        - **Silurian Period (~420 Mya)**: First fungal structures.
        - **Devonian Period (~400 Mya)**: Early plant-fungi relationships.
        - **Cretaceous Period (~90 Mya)**: First modern mushrooms.
        """)
    with st.expander("🦠 **Fossil Finds**"):
        st.write("""
        - **Prototaxites**: Largest terrestrial organism of the Silurian.
        - **Archaeomarasmius**: Oldest known basidiomycete (~90 Mya).
        """)

    # Section 9:Ecology and Habitat of Mushrooms
    st.header("🌿 Ecology and Habitat of Mushrooms")
    st.write("""
    Mushrooms play a crucial role in nature by breaking down organic material, forming partnerships with plants, and supporting ecosystems. 
    They thrive in **forests, grasslands, deserts, aquatic environments, and even cities!**
    """)
    with st.expander("🌳 **Terrestrial Habitats**"):
        st.markdown("""
        - **Forests**: Decompose organic matter and form symbiotic relationships with trees.
        - **Grasslands**: Improve soil fertility and break down dead plants.
        - **Deserts**: Survive extreme conditions with special adaptations.
        """)
    with st.expander("💧 **Aquatic Habitats**"):
        st.write("Some mushrooms have adapted to wet or semi-aquatic conditions.")
    with st.expander("🏙️ **Urban Environments**"):
        st.write("Mushrooms can grow in unexpected places, including roadsides, gardens, and compost piles!")

    #  Section 10:Mushroom Cultivation
    st.header("🌱 Mushroom Cultivation")
    st.write("""
    Mushroom cultivation involves growing mushrooms under controlled conditions for food, medicine, and industrial applications.
    """)
    with st.expander("🌾 **Steps for Growing Mushrooms**"):
        st.markdown("""
        1. **Substrate Preparation**: Use straw, wood chips, or compost.
        2. **Inoculation**: Introduce mushroom spores or mycelium.
        3. **Incubation**: Allow the mycelium to colonize the substrate.
        4. **Fruiting**: Provide the right conditions for mushrooms to grow.
        5. **Harvesting**: Pick mushrooms when the caps are fully open.
        """)
    with st.expander("🏡 **Popular Species for Cultivation**"):
        st.write("""
        - **Oyster Mushrooms**: Easy to grow and fast-growing.
        - **Shiitake Mushrooms**: Grown on hardwood logs or sawdust blocks.
        - **Button Mushrooms**: Grown on composted manure.
        """)

    # Section 11: Uses of Mushrooms
    st.header("🍄 Uses of Mushrooms")
    st.write("""
    Mushrooms have been used by humans for thousands of years for food, medicine, and cultural practices.
    """)
    with st.expander("🍽️ **Culinary Uses**"):
        st.markdown("""
        - **Cooking**: Used in soups, stir-fries, and sauces.
        - **Meat Substitutes**: Mushrooms like portobello are used as vegetarian alternatives.
        """)
    with st.expander("💊 **Medicinal Uses**"):
        st.markdown("""
        - **Immune Support**: Reishi and chaga boost the immune system.
        - **Cognitive Health**: Lion's mane supports brain function.
        """)
    with st.expander("🏭 **Industrial Uses**"):
        st.write("""
        - **Bioremediation**: Mushrooms clean up pollutants like oil spills.
        - **Biodegradable Materials**: Mycelium is used to create eco-friendly packaging.
        """)

    # Section 12: Toxicity and Safety
    st.header("⚠️ Mushroom Toxicity and Safety")
    st.write("""
    While mushrooms provide numerous benefits, they also pose significant health risks if improperly identified or consumed.
    """)
    with st.expander("🔍 **Identifying Poisonous Mushrooms**"):
        st.markdown("""
        - **Key Features**: Cap shape, gills, stem, and spore print.
        - **Common Mistakes**: Confusing edible mushrooms with toxic look-alikes.
        """)
    with st.expander("🚨 **Symptoms of Mushroom Poisoning**"):
        st.markdown("""
        - Nausea, vomiting, diarrhea, liver failure, or death (in severe cases).
        """)

    # Section 13: Cultural and Historical Significance
    st.header("📜 Cultural and Historical Significance")
    st.write("""
    Mushrooms have influenced human history, culture, and spirituality for thousands of years.
    """)
    with st.expander("🌍 **Traditional Uses**"):
        st.markdown("""
        - **Chinese Medicine**: Reishi and cordyceps have been used for centuries.
        - **Native American Rituals**: Psychedelic mushrooms used in spiritual practices.
        """)
    with st.expander("📖 **Folklore and Myths**"):
        st.markdown("""
        - **Fairy Rings**: Associated with fairies in European folklore.
        - **Fly Agaric**: Linked to Santa Claus and Christmas traditions.
        """)

    # Section 14: Research and Biotechnology
    st.header("🔬 Research and Biotechnology")
    st.write("""
    Mushrooms are a major focus of modern scientific research and technological innovation.
    """)
    with st.expander("🧪 **Current Research**"):
        st.markdown("""
        - **Psychedelic Therapy**: Studies on psilocybin for treating depression and PTSD.
        - **Fungal Networks**: Research on the "Wood Wide Web" and mycorrhizal relationships.
        """)
    with st.expander("⚙️ **Biotechnological Applications**"):
        st.markdown("""
        - **Enzyme Production**: Fungi used to produce industrial enzymes.
        - **Biofuels**: Mushrooms explored as a source of renewable energy.
        """)

    # Section 15: Conservation and Ethics
    st.header("🌿 Conservation and Ethics")
    st.write("""
    Mushrooms play a crucial ecological role, but many species are threatened by habitat destruction, pollution, and overharvesting.
    """)
    with st.expander("⚠️ **Threats to Mushroom Species**"):
        st.markdown("""
        - **Habitat Loss**: Deforestation and urbanization.
        - **Climate Change**: Altered rainfall and temperature.
        - **Overharvesting**: High demand for edible and medicinal mushrooms.
        """)
    with st.expander("🌱 **Conservation Efforts**"):
        st.markdown("""
        - **Protected Areas**: Establishing reserves for fungal biodiversity.
        - **Sustainable Harvesting**: Promoting ethical foraging practices.
        """)

    # Section 16: Education and Careers
    st.header("🎓 Education and Careers")
    st.write("""
    Mycology—the scientific study of fungi—is a growing field with expanding educational programs and career opportunities.
    """)
    with st.expander("📚 **Educational Programs**"):
        st.markdown("""
        - **Undergraduate Degrees**: Offered in biology, environmental science, and microbiology.
        - **Graduate Degrees**: Master’s and Ph.D. programs in mycology and fungal genetics.
        """)
    with st.expander("💼 **Career Opportunities**"):
        st.markdown("""
        - **Mushroom Farmer**: Growing edible and medicinal mushrooms.
        - **Mycologist**: Researching fungal biology and taxonomy.
        - **Biotechnologist**: Developing fungal-based materials and medicines.
        """)

 # Section 17: Interesting Facts
    st.header("🤯 Interesting Facts")
    st.markdown("""
    - **Largest Living Organism**: The Honey Fungus (*Armillaria ostoyae*) spans over 2,300 acres in Oregon.  
    - **Bioluminescence**: Mushrooms like *Mycena chlorophos* glow in the dark due to chemical reactions.  
    - **Ancient Fossils**: Fossilized mushrooms over 115 million years old have been found.  
    - **Hallucinogenic History**: Used in ancient spiritual rituals by cultures like the Aztecs.  
    - **Natural Antibiotics**: Penicillin, the first antibiotic, was derived from fungi.  
    """)
# Section 18: Warnings for Mushroom Foragers
    st.header("⚠️ Warnings for Mushroom Foragers")
    st.markdown("""
    - **Identification Skills**: Many edible mushrooms have toxic look-alikes. Use expert guides or consult professionals.  
    - **Cooking Requirement**: Some edible mushrooms are toxic when raw, such as morels.  
    - **Seasonality**: Mushrooms grow during specific times, often in symbiosis with particular trees.  
    """)
# Section 19: Why Mushroom Classification is Important
    st.header("🌟 Why Mushroom Classification is Important")
    st.write(
        """
        🍄 Mushrooms are widely consumed as **food** 🍽️ around the world.  
        However, many species of mushrooms are **poisonous** ☠️ and can lead to severe **health issues** 🤒 or even **death** 💀 if consumed.  
        ✅ Accurate mushroom identification is essential to protect **human health** 🛡️ and avoid **poisoning** ⚠️.  

        ### 🎯 The two models developed in this project aim to help:
        - **🍽️ Identify Edible Mushrooms**: By classifying mushrooms based on physical characteristics, we help users determine which mushrooms are **safe for consumption** ✅.  
        - **☠️ Avoid Toxic Mushrooms**: Toxic mushrooms are often mistaken for edible ones, causing **dangerous consequences** 🚫. Our model helps differentiate them based on specific features.  

        ### 🌍 In a broader sense, mushroom classification can also support:
        - **🔬 Mushroom Research**: Helping scientists 🧪 better categorize and study mushrooms.  
        - **🍄 Mushroom Enthusiasts**: Providing an accessible tool for hobbyists 🏕️ and foragers 🌲 to safely explore mushrooms in the wild.  
        - **🌱 Environmental Impact**: Understanding mushroom ecosystems helps maintain **ecological balance** 🌍.  
        - **📚 Educational Tool**: Encourages learning about mushroom diversity and safety.  

        🚀 With growing interest in mushroom-based nutrition and medicine, this project contributes to both **scientific research** and **public safety**.  
        """
    )
# Section 20: Safety Precautions & Warnings
    st.header("Safety Precautions & Warnings")
    st.write(
        """
        Even though this project aims to classify mushrooms as either edible or poisonous, users should still exercise caution. Our system provides predictions based on input features and machine learning models, but it is not a replacement for expert advice.

        **Always consult an expert mycologist or use additional resources before consuming any wild mushrooms.**

        This tool should be used as an educational aid and a first step in mushroom identification. Don't rely solely on the results from the model—cross-check with trusted resources.
        """
    )
    # Footer with social links
    st.markdown('<div class="footer">Created with ❤️ by Strategic Synergists </div>', unsafe_allow_html=True)