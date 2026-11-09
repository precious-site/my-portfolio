import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

files = {
    "package.json": """
{
  "name": "abhishek-portfolio",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "framer-motion": "^10.16.4",
    "jspdf": "^2.5.1",
    "lucide-react": "^0.292.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.37",
    "@types/react-dom": "^18.2.15",
    "@vitejs/plugin-react": "^4.2.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.31",
    "tailwindcss": "^3.3.5",
    "vite": "^5.0.0"
  }
}
""",
    "vite.config.js": """
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
""",
    "tailwind.config.js": """
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        dark: {
          bg: '#0a0a0f',
          surface: '#12121a',
          accent: '#1b1448', 
        },
        light: {
          bg: '#faf9f6',
          surface: '#ffffff',
          accent: '#f3f4f6',
        },
        primary: '#d4af37', // Subtle metallic gold
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
        display: ['"Playfair Display"', 'serif'],
      },
      transitionProperty: {
        'height': 'height',
        'spacing': 'margin, padding',
      }
    },
  },
  plugins: [],
}
""",
    "postcss.config.js": """
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
""",
    "index.html": """
<!doctype html>
<html lang="en" class="scroll-smooth">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Abhishek Yadav | MERN Stack Developer</title>
    <meta name="description" content="Portfolio of Abhishek Yadav, a premium MERN Stack Developer specializing in sophisticated, high-performance web applications." />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
  </head>
  <body class="bg-light-bg dark:bg-dark-bg text-gray-900 dark:text-gray-100 transition-colors duration-300 antialiased selection:bg-primary selection:text-white">
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
""",
    "src/index.css": """
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer utilities {
  .glass {
    @apply bg-white/70 dark:bg-[#12121a]/70 backdrop-blur-md border border-gray-200/50 dark:border-white/5;
  }
  .glass-card {
    @apply bg-white dark:bg-dark-surface border border-gray-100 dark:border-white/5 shadow-sm dark:shadow-none hover:shadow-md transition-shadow duration-300;
  }
}
""",
    "src/main.jsx": """
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
""",
    "src/utils/generateResume.js": """
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
""",
    "src/App.jsx": """
import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Expertise from './components/Expertise';
import Projects from './components/Projects';
import Experience from './components/Experience';
import Contact from './components/Contact';
import Footer from './components/Footer';

function App() {
  const [theme, setTheme] = useState('dark');

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      setTheme(savedTheme);
      document.documentElement.classList.toggle('dark', savedTheme === 'dark');
    } else {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.classList.toggle('dark');
  };

  return (
    <div className="min-h-screen font-sans selection:bg-primary selection:text-white">
      <Navbar theme={theme} toggleTheme={toggleTheme} />
      <main>
        <Hero />
        <About />
        <Expertise />
        <Projects />
        <Experience />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}

export default App;
""",
    "src/components/Navbar.jsx": """
import React, { useState, useEffect } from 'react';
import { Moon, Sun, Menu, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const Navbar = ({ theme, toggleTheme }) => {
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'About', href: '#about' },
    { name: 'Expertise', href: '#expertise' },
    { name: 'Work', href: '#work' },
    { name: 'Contact', href: '#contact' },
  ];

  return (
    <header className={`fixed top-0 w-full z-50 transition-all duration-300 ${scrolled ? 'glass py-4' : 'bg-transparent py-6'}`}>
      <div className="max-w-7xl mx-auto px-6 md:px-12 flex justify-between items-center">
        <a href="#" className="font-display font-semibold text-xl tracking-tight">AY.</a>
        
        <nav className="hidden md:flex items-center gap-8 text-sm font-medium">
          {navLinks.map((link) => (
            <a key={link.name} href={link.href} className="text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary transition-colors">
              {link.name}
            </a>
          ))}
          <button onClick={toggleTheme} className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-white/10 transition-colors" aria-label="Toggle Theme">
            {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
          </button>
        </nav>

        <div className="md:hidden flex items-center gap-4">
          <button onClick={toggleTheme} className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-white/10 transition-colors">
            {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
          </button>
          <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className="p-2">
            {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </div>

      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="absolute top-full left-0 w-full glass border-t border-gray-200 dark:border-white/5 py-4 px-6 flex flex-col gap-4 md:hidden shadow-lg"
          >
            {navLinks.map((link) => (
              <a 
                key={link.name} 
                href={link.href} 
                onClick={() => setMobileMenuOpen(false)}
                className="text-lg font-medium text-gray-800 dark:text-gray-200"
              >
                {link.name}
              </a>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
};

export default Navbar;
""",
    "src/components/Hero.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Download } from 'lucide-react';
import { downloadResume } from '../utils/generateResume';

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center pt-20 overflow-hidden">
      <div className="absolute inset-0 z-0 opacity-30 dark:opacity-20 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-[#1b1448] via-transparent to-transparent"></div>
      
      <div className="max-w-7xl mx-auto px-6 md:px-12 w-full z-10 grid md:grid-cols-2 gap-12 items-center">
        <motion.div 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="flex flex-col gap-6"
        >
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-gray-200 dark:border-white/10 w-fit text-xs font-medium tracking-wide uppercase">
            <span className="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
            Available for new opportunities
          </div>
          
          <h1 className="font-display text-5xl md:text-7xl font-medium leading-[1.1] tracking-tight text-gray-900 dark:text-white">
            Quiet Luxury.<br/>
            <span className="text-gray-400 dark:text-gray-500">Technical Excellence.</span>
          </h1>
          
          <p className="text-lg md:text-xl text-gray-600 dark:text-gray-400 max-w-lg leading-relaxed font-light">
            I am Abhishek Yadav, a MERN Stack Developer engineering sophisticated, high-performance digital experiences.
          </p>
          
          <div className="flex flex-wrap items-center gap-4 mt-4">
            <a href="#work" className="inline-flex items-center justify-center gap-2 bg-gray-900 dark:bg-white text-white dark:text-gray-900 px-6 py-3 rounded-none text-sm font-medium hover:bg-primary dark:hover:bg-primary hover:text-white dark:hover:text-white transition-all duration-300">
              Explore My Work <ArrowRight size={16} />
            </a>
            <button onClick={downloadResume} className="inline-flex items-center justify-center gap-2 bg-transparent border border-gray-300 dark:border-white/20 text-gray-900 dark:text-white px-6 py-3 rounded-none text-sm font-medium hover:bg-gray-50 dark:hover:bg-white/5 transition-all duration-300">
              Download Résumé <Download size={16} />
            </button>
          </div>
        </motion.div>

        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.2 }}
          className="relative h-[60vh] md:h-[80vh] w-full hidden md:block"
        >
          <div className="absolute inset-0 bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 overflow-hidden">
            {/* If user provides profile.jpg in public folder, it will load here. Otherwise falls back to elegant abstract. */}
            <img 
              src="/profile.jpg" 
              alt="Abhishek Yadav" 
              className="w-full h-full object-cover object-center grayscale hover:grayscale-0 transition-all duration-700"
              onError={(e) => {
                e.target.style.display = 'none';
                e.target.nextSibling.style.display = 'block';
              }}
            />
            <div className="hidden w-full h-full bg-gradient-to-tr from-[#1b1448]/20 to-transparent"></div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Hero;
""",
    "src/components/About.jsx": """
import React from 'react';
import { motion } from 'framer-motion';

const About = () => {
  return (
    <section id="about" className="py-24 md:py-32 bg-white dark:bg-dark-bg">
      <div className="max-w-7xl mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="grid md:grid-cols-12 gap-12"
        >
          <div className="md:col-span-4">
            <h2 className="text-xs font-semibold tracking-widest uppercase text-gray-400 dark:text-gray-500 mb-4">Biography</h2>
            <h3 className="font-display text-3xl md:text-4xl text-gray-900 dark:text-white">Effortless Sophistication in Code.</h3>
          </div>
          
          <div className="md:col-span-8 flex flex-col gap-6 text-gray-600 dark:text-gray-300 text-lg leading-relaxed font-light">
            <p>
              I am Abhishek Yadav, a passionate MERN Stack Developer with an uncompromising dedication to building modern, responsive, and user-centric web applications.
            </p>
            <p>
              My expertise lies in full-stack architecture utilizing MongoDB, Express.js, React.js, and Node.js. I approach software engineering not just as writing code, but as crafting premium digital solutions that solve complex problems with elegant simplicity.
            </p>
            <p>
              Whether structuring robust backend APIs or designing intuitive frontend interfaces, my focus remains on scalability, technical excellence, and continuous growth.
            </p>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default About;
""",
    "src/components/Expertise.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import { Code2, Database, Layout, Terminal } from 'lucide-react';

const skills = [
  {
    category: "Frontend Engineering",
    icon: <Layout className="w-6 h-6 mb-4 text-primary" />,
    items: ["React.js & Hooks", "JavaScript (ES6+)", "Tailwind CSS", "HTML5 & CSS3", "Bootstrap", "Responsive Design"]
  },
  {
    category: "Backend Architecture",
    icon: <Terminal className="w-6 h-6 mb-4 text-primary" />,
    items: ["Node.js", "Express.js", "RESTful APIs", "JWT Authentication", "CRUD Operations", "API Integration"]
  },
  {
    category: "Database Management",
    icon: <Database className="w-6 h-6 mb-4 text-primary" />,
    items: ["MongoDB", "Mongoose", "MySQL", "Data Modeling", "Query Optimization"]
  },
  {
    category: "Development Tools",
    icon: <Code2 className="w-6 h-6 mb-4 text-primary" />,
    items: ["Git & GitHub", "VS Code", "Postman", "npm/Yarn", "Vercel Deployment"]
  }
];

const Expertise = () => {
  return (
    <section id="expertise" className="py-24 md:py-32 bg-gray-50 dark:bg-[#0d0d14]">
      <div className="max-w-7xl mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-16"
        >
          <h2 className="text-xs font-semibold tracking-widest uppercase text-gray-400 dark:text-gray-500 mb-4">Technical Arsenal</h2>
          <h3 className="font-display text-3xl md:text-4xl text-gray-900 dark:text-white">Precision Tools & Technologies.</h3>
        </motion.div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {skills.map((skill, index) => (
            <motion.div 
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              className="glass-card p-8 group"
            >
              {skill.icon}
              <h4 className="text-lg font-medium text-gray-900 dark:text-white mb-4">{skill.category}</h4>
              <ul className="space-y-2">
                {skill.items.map((item, i) => (
                  <li key={i} className="text-sm text-gray-600 dark:text-gray-400 font-light flex items-center before:content-[''] before:w-1 before:h-1 before:bg-gray-300 dark:before:bg-gray-600 before:rounded-full before:mr-2">
                    {item}
                  </li>
                ))}
              </ul>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Expertise;
""",
    "src/components/Projects.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import { ExternalLink, Github } from 'lucide-react';

const projects = [
  {
    title: "Enterprise MERN Dashboard",
    description: "A comprehensive administrative dashboard built with React, Node, Express, and MongoDB. Features secure JWT authentication, real-time data visualization, and advanced CRUD capabilities for large-scale data management.",
    tech: ["React", "Node.js", "MongoDB", "Tailwind CSS"],
    liveLink: "#",
    githubLink: "https://github.com/Abh1sh3ky",
    image: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
  },
  {
    title: "E-Commerce Architecture",
    description: "A scalable digital storefront infrastructure handling complex state management, integrated payment gateways, and a responsive shopping cart experience.",
    tech: ["MERN Stack", "Redux", "Stripe API"],
    liveLink: "#",
    githubLink: "https://github.com/Abh1sh3ky",
    image: "https://images.unsplash.com/photo-1661956602116-aa6865609028?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
  }
];

const Projects = () => {
  return (
    <section id="work" className="py-24 md:py-32 bg-white dark:bg-dark-bg">
      <div className="max-w-7xl mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.7 }}
              className={`flex flex-col ${index % 2 !== 0 ? 'md:flex-row-reverse' : 'md:flex-row'} gap-8 md:gap-16 items-center`}
            >
              <div className="w-full md:w-3/5 overflow-hidden bg-gray-100 dark:bg-white/5 border border-gray-100 dark:border-white/10 group">
                <img 
                  src={project.image} 
                  alt={project.title} 
                  className="w-full h-[400px] object-cover object-center grayscale hover:grayscale-0 transition-all duration-700 transform group-hover:scale-105"
                />
              </div>
              
              <div className="w-full md:w-2/5 flex flex-col gap-6">
                <div className="flex flex-wrap gap-2 mb-2">
                  {project.tech.map((t, i) => (
                    <span key={i} className="text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">{t}</span>
                  ))}
                </div>
                <h4 className="font-display text-2xl md:text-3xl text-gray-900 dark:text-white">{project.title}</h4>
                <p className="text-gray-600 dark:text-gray-300 font-light leading-relaxed">
                  {project.description}
                </p>
                <div className="flex items-center gap-6 mt-4">
                  <a href={project.liveLink} className="text-sm font-medium border-b border-gray-900 dark:border-white hover:text-primary hover:border-primary dark:hover:text-primary dark:hover:border-primary transition-colors flex items-center gap-2 pb-1">
                    View Live <ExternalLink size={14} />
                  </a>
                  <a href={project.githubLink} className="text-sm font-medium text-gray-500 hover:text-gray-900 dark:hover:text-white transition-colors flex items-center gap-2">
                    Source Code <Github size={14} />
                  </a>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Projects;
""",
    "src/components/Experience.jsx": """
import React from 'react';
import { motion } from 'framer-motion';

const Experience = () => {
  return (
    <section className="py-24 md:py-32 bg-gray-50 dark:bg-[#0d0d14]">
      <div className="max-w-7xl mx-auto px-6 md:px-12 grid md:grid-cols-2 gap-16">
        
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}>
          <h2 className="font-display text-2xl mb-8 text-gray-900 dark:text-white border-b border-gray-200 dark:border-white/10 pb-4">Professional Experience</h2>
          <div className="relative pl-6 border-l border-gray-200 dark:border-white/10">
            <div className="absolute w-3 h-3 bg-gray-200 dark:bg-white/20 rounded-full -left-[6.5px] top-2"></div>
            <h4 className="text-lg font-medium text-gray-900 dark:text-white">Full Stack Development Focus</h4>
            <p className="text-sm text-primary mb-3">Independent | Present</p>
            <p className="text-sm text-gray-600 dark:text-gray-400 font-light leading-relaxed">
              Actively conceptualizing, architecting, and deploying sophisticated MERN stack applications. Focus on building scalable data structures, implementing secure JWT authentication, and designing responsive, accessible user interfaces.
            </p>
          </div>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: 0.2 }}>
          <h2 className="font-display text-2xl mb-8 text-gray-900 dark:text-white border-b border-gray-200 dark:border-white/10 pb-4">Education & Certifications</h2>
          <div className="relative pl-6 border-l border-gray-200 dark:border-white/10">
            <div className="absolute w-3 h-3 bg-gray-200 dark:bg-white/20 rounded-full -left-[6.5px] top-2"></div>
            <h4 className="text-lg font-medium text-gray-900 dark:text-white">Computer Science Fundamentals</h4>
            <p className="text-sm text-primary mb-3">India</p>
            <p className="text-sm text-gray-600 dark:text-gray-400 font-light leading-relaxed">
              Comprehensive study of algorithmic problem solving, database management systems (SQL/NoSQL), and modern software engineering principles, forming the foundation of robust web development.
            </p>
          </div>
        </motion.div>

      </div>
    </section>
  );
};

export default Experience;
""",
    "src/components/Contact.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import { Mail, Phone, MapPin, Github, Linkedin } from 'lucide-react';

const Contact = () => {
  return (
    <section id="contact" className="py-24 md:py-32 bg-white dark:bg-dark-bg">
      <div className="max-w-7xl mx-auto px-6 md:px-12 grid md:grid-cols-2 gap-16">
        
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}>
          <h2 className="text-xs font-semibold tracking-widest uppercase text-gray-400 dark:text-gray-500 mb-4">Get In Touch</h2>
          <h3 className="font-display text-4xl md:text-5xl text-gray-900 dark:text-white mb-8">Let's build the extraordinary.</h3>
          <p className="text-gray-600 dark:text-gray-400 font-light leading-relaxed mb-12 max-w-md">
            I am currently open to new opportunities and international collaborations. Whether you have a project in mind or simply want to connect, my inbox is always open.
          </p>
          
          <div className="flex flex-col gap-6">
            <a href="mailto:abhi997353@gmail.com" className="flex items-center gap-4 text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary transition-colors group">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-none group-hover:border-primary transition-colors"><Mail size={18} /></span>
              <span className="font-medium">abhi997353@gmail.com</span>
            </a>
            <div className="flex items-center gap-4 text-gray-600 dark:text-gray-300">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-none"><Phone size={18} /></span>
              <span className="font-medium">+91 9973530779</span>
            </div>
            <div className="flex items-center gap-4 text-gray-600 dark:text-gray-300">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-none"><MapPin size={18} /></span>
              <span className="font-medium">India</span>
            </div>
          </div>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: 0.2 }} className="glass p-8 md:p-12">
          <form className="flex flex-col gap-6">
            <div className="flex flex-col gap-2">
              <label className="text-xs uppercase tracking-wider text-gray-500">Name</label>
              <input type="text" className="w-full bg-transparent border-b border-gray-300 dark:border-white/20 pb-2 text-gray-900 dark:text-white focus:outline-none focus:border-primary dark:focus:border-primary transition-colors rounded-none" />
            </div>
            <div className="flex flex-col gap-2">
              <label className="text-xs uppercase tracking-wider text-gray-500">Email</label>
              <input type="email" className="w-full bg-transparent border-b border-gray-300 dark:border-white/20 pb-2 text-gray-900 dark:text-white focus:outline-none focus:border-primary dark:focus:border-primary transition-colors rounded-none" />
            </div>
            <div className="flex flex-col gap-2">
              <label className="text-xs uppercase tracking-wider text-gray-500">Message</label>
              <textarea rows="4" className="w-full bg-transparent border-b border-gray-300 dark:border-white/20 pb-2 text-gray-900 dark:text-white focus:outline-none focus:border-primary dark:focus:border-primary transition-colors resize-none rounded-none"></textarea>
            </div>
            <button type="button" className="mt-4 bg-gray-900 dark:bg-white text-white dark:text-gray-900 py-4 font-medium text-sm hover:bg-primary dark:hover:bg-primary hover:text-white transition-colors duration-300 w-full rounded-none">
              Send Message
            </button>
          </form>
        </motion.div>

      </div>
    </section>
  );
};

export default Contact;
""",
    "src/components/Footer.jsx": """
import React from 'react';
import { Github, Linkedin, ArrowUp } from 'lucide-react';

const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="border-t border-gray-200 dark:border-white/5 bg-white dark:bg-dark-bg py-8">
      <div className="max-w-7xl mx-auto px-6 md:px-12 flex flex-col md:flex-row justify-between items-center gap-4">
        <p className="text-sm text-gray-500 dark:text-gray-400 font-light">
          &copy; {new Date().getFullYear()} Abhishek Yadav. All rights reserved.
        </p>
        
        <div className="flex items-center gap-6">
          <a href="https://github.com/Abh1sh3ky" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
            <Github size={20} />
          </a>
          <a href="https://www.linkedin.com/in/abhishek-yadav-63089b271" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
            <Linkedin size={20} />
          </a>
          <button onClick={scrollToTop} className="ml-4 p-2 bg-gray-100 dark:bg-white/5 rounded-none text-gray-500 hover:text-gray-900 dark:hover:text-white transition-colors">
            <ArrowUp size={16} />
          </button>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
"""
}

for file_path, content in files.items():
    create_file(file_path, content)
    print(f"Created: {file_path}")

print("\nSuccess: Enterprise Portfolio Architecture Generated.")
