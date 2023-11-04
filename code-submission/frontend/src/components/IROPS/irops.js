import React from "react";
import "./irops.css";
import IropsData from "./iropsData";
import img1 from "../../assets/storm.jpg";
import img2 from "../../assets/plane-checkup.jpg";
import img3 from "../../assets/DFW.jpg";


function IROPS() {
  return (
  <>
    
    <div className="irops-info">
      <h1 className="irops-title">Why flights are canceled</h1>

      <div className="irops-info-card">
        <IropsData
          image={img1}
          link="https://www.google.com"
          heading="Weather"
          text="Bad weather can lead to cancellations. Conditions like thunderstorms, snowstorms, heavy rain, 
          strong winds, and fog can significantly impact the safety of air travel. These weather conditions can affect a pilot's ability to take off, navigate, and land the aircraft safely. For instance, low visibility due to fog or heavy rain blurs the runway and impairs the pilot's sight.
          In such situations, airlines may choose to cancel flights to ensure passengers' 
          safety. As the winter season peaked in 2022 with temperature falling below -10C, 
          the authorities at Stansted Airport had every flight cancelled due to weather. -Air Advisor"
        />
        
        <IropsData
          image={img2}
          link="https://www.google.com"
          heading="Aircraft Conditions"
          text="Flight cancellation due to aircraft technical issues is not uncommon. 
          The procedure that determines these conditions is called a checklist, a 
          list of tasks and behaviors that must be followed before, during, and 
          after the operation in order to ensure the operational safety of the 
          flight. This procedure, in short, consists of a detailed observation of 
          all the items present on a detailed list, a process that takes time and 
          must be undertaken to prevent any problems on a flight. -Fly Flapper" 
        />
        <IropsData
          image={img3}
          link="https://www.google.com"
          heading="Tight flight schedule"
          text="Tight flight schedules refer to the scheduling of flights 
          with very little time between arrivals and departures. One of the 
          most common reasons why tight flight schedules can cause flight 
          disruptions is because of the knock-on effect of delays.
          If one flight is delayed due to unforeseen circumstances such as 
          weather, mechanical issues, or crew scheduling conflicts, it can impact the entire schedule for the day. Passengers may miss their connections or have to be rebooked onto other flights, which can lead to cancellations.    
          Additionally, crew scheduling conflicts can also cause issues with 
          tight flight schedules. -Air Advisor"
        />
      </div>
    </div>
    </>
    );
  
}

export default IROPS;
