import React from 'react';
import image1 from "./AlpineForest.png";
import image2 from "./DryTropicalForest.png";
import image3 from "./MontaneTemperteForest.png";
import image4 from "./MontaneSubtropicalForest.png";
import image5 from "./MositTropicalForest.png";

const Image = () => {
    return (
        <div>
            if ({text} === "Montane temperte forest") {
                <img src={image3} alt="" />
            }
            if ({text} === "Alpine forest") {
                <img src={image1} alt="" />
            }
            if ({text} === "Moist Tropical forest") {
                <img src={image3} alt="" />
            }
            if ({text} === "Dry tropical forest") {
                <img src={image2} alt="" />

            }
            if ({text} === "Montane sub tropical forest") {
                <img src={image4} alt="" />

            }
        </div>
    );
}

export default Image;
