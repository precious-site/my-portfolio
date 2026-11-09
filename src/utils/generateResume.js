import { jsPDF } from "jspdf";

export const downloadResume = () => {
  const doc = new jsPDF();
  
  doc.setFont("helvetica", "bold");
  doc.setFontSize(24);
  doc.setTextColor(27, 20, 72); // Midnight blue
  doc.text("ABHISHEK YADAV", 20, 30);
  
  doc.setFont("helvetica", "normal");
  doc.setFontSize(12);
  doc.setTextColor(100, 100, 100);
  doc.text("MERN Stack Developer | Full Stack Web Developer", 20, 40);
  
  doc.setFontSize(10);
  doc.text("Email: abhi997353@gmail.com | Phone: 9973530779 | Location: India", 20, 48);
  doc.text("GitHub: github.com/Abh1sh3ky | LinkedIn: linkedin.com/in/abhishek-yadav-63089b271", 20, 54);
  
  doc.setDrawColor(200, 200, 200);
  doc.line(20, 60, 190, 60);
  
  doc.setFont("helvetica", "bold");
  doc.setFontSize(14);
  doc.setTextColor(0, 0, 0);
  doc.text("PROFESSIONAL SUMMARY", 20, 75);
  
  doc.setFont("helvetica", "normal");
  doc.setFontSize(10);
  doc.setTextColor(50, 50, 50);
  const summary = doc.splitTextToSize(
    "Passionate MERN Stack Developer with an interest in building modern, responsive, and user-friendly web applications. Specializing in full-stack web development using MongoDB, Express.js, React.js, and Node.js.", 
    170
  );
  doc.text(summary, 20, 85);
  
  doc.setFont("helvetica", "bold");
  doc.setFontSize(14);
  doc.setTextColor(0, 0, 0);
  doc.text("TECHNICAL SKILLS", 20, 110);
  
  doc.setFont("helvetica", "normal");
  doc.setFontSize(10);
  doc.setTextColor(50, 50, 50);
  doc.text("Frontend: HTML5, CSS3, JavaScript (ES6+), React.js, Tailwind CSS, Bootstrap", 20, 120);
  doc.text("Backend: Node.js, Express.js, REST APIs, JWT Authentication", 20, 128);
  doc.text("Database: MongoDB, Mongoose, MySQL", 20, 136);
  doc.text("Tools: Git, GitHub, VS Code, Postman, npm", 20, 144);
  
  doc.setFont("helvetica", "bold");
  doc.setFontSize(14);
  doc.setTextColor(0, 0, 0);
  doc.text("EXPERIENCE & PROJECTS", 20, 160);
  
  doc.setFont("helvetica", "normal");
  doc.setFontSize(10);
  doc.setTextColor(50, 50, 50);
  const expText = doc.splitTextToSize(
    "Currently focusing on MERN Stack Development, executing practical full-stack projects, building scalable applications, and developing robust RESTful APIs with secure authentication layers.", 
    170
  );
  doc.text(expText, 20, 170);
  
  doc.save("Abhishek_Yadav_Resume.pdf");
};