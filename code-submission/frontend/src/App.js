import "./styles.css";
import { Route, Routes } from "react-router-dom";
import Home from "./routes/ReCancellation";
import About from "./routes/PostCancellation";
export default function App() {
  return (
    <div className="App">
      
      <Routes>
        <Route path="/" element={<PreCancellation />}/>
        <Route path="/post-cancellation" element={<PostCancellation />}/>       
      </Routes>
      
      
      
    </div>
  );
}