import "./Footer.css";
import logo from "../../assets/ww1.png"

const Footer = () => {
  return (
    <div className="footer">
      <div className="top">
        <div className="centered">
        <img src={logo} alt="logo"/>
          <h1>Weather Wise</h1>
          <p>Know Before You Go</p>
          <h3>Created By Dude Spelman for BE Hackathon 2023</h3>
        </div>
      </div>

      <div className="bottom"></div>

    </div>
  );
};

export default Footer;