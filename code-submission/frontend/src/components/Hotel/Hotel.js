import "./HPCInfoStyles.css";
import HPCInfoData from "./HPCInfoData";
import Trip1 from "../assets/5.jpg";
import Trip2 from "../assets/8.jpg";
import Trip3 from "../assets/6.jpg";
import img1 from "../assets/Linux-Logo.png"
import img2 from "../assets/s2.jpg"
import img3 from "../assets/Top500_logo.png"
function HPCInfo() {
  return (
    <>
    <div className="hpc-info">
      <h1>Learn HPC Today</h1>
      <p>Learn the basics of Linux/Unix commands necessary 
        for Morehouse HPC</p>

        <div className="hpc-info-card">
          <HPCInfoData 
          image={img1}
          link="https://www.freecodecamp.org/news/the-linux-commands-handbook/"
          heading="Learn the commands"
          text="Linux commands are essential tools used 
          for tasks like job submission, cluster management, 
          file manipulation, and software installation, 
          as Linux is the dominant operating system in HPC 
          environments.These commands enable users to harness the 
          computational capabilities of HPC clusters efficiently and effectively."
          
          
          />
          <HPCInfoData 
          image={img2}
          link="https://builtin.com/hardware/high-performance-computing-applications"
          heading="Understanding the Industry"
          text="Take a look into how HPC plays a role in the industry. 
          Even if you're just hearing about HPC now, it has a role nearly 
          everything we interact with everyday."
          
          
          />
          <HPCInfoData 
          image={img3}
          link="https://www.top500.org/"
          heading="TOP500"
          text="Delve into this prestigious ranking to discover the most powerful 
          supercomputers on the planet. From breakthroughs in scientific research 
          to driving innovation across industries, these computational giants are 
          paving the way to a brighter future. Explore the Top500 HPC list today 
          and witness the incredible power of human achievement in the digital age."
          />

        </div>
    </div>
  
    
    </>
  );
}

export default HPCInfo;