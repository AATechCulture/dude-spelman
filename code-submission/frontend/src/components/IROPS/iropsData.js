import "./irops.css";
import { Link } from "react-router-dom";
function IropsData(props){
    return(
        <div className="irops-card">
      <div className="irops-image">
        <Link to={props.link} target="_blank">
        <img src={props.image} alt="image" />
        </Link>
      </div>
      <h4>{props.heading}</h4>
      <p>{props.text}</p>
    </div>
        
    );
}

export default IropsData;
