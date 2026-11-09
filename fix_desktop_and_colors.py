import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

files = {
    "src/components/Hero.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Download, Code } from 'lucide-react';
import { downloadResume } from '../utils/generateResume';

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center pt-24 pb-12 overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 md:px-12 w-full z-10 grid md:grid-cols-2 gap-12 md:gap-8 items-center">
        
        {/* Left Side - Text & CTA (Desktop & Tablet) */}
        <motion.div 
          initial={{ opacity: 0, x: -30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="flex flex-col gap-6 order-1"
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-neon-purple/30 bg-neon-purple/5 backdrop-blur-md w-fit text-xs font-semibold tracking-wide uppercase text-neon-purple dark:text-neon-cyan shadow-[0_0_15px_rgba(139,92,246,0.15)]">
            <span className="w-2 h-2 rounded-full bg-neon-purple dark:bg-neon-cyan animate-pulse"></span>
            Available for new opportunities
          </div>
          
          <h1 className="font-display text-5xl md:text-7xl font-bold leading-[1.1] tracking-tight text-gray-900 dark:text-white">
            Abhishek <span className="text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple">Kumar</span>
          </h1>
          <h2 className="text-2xl md:text-4xl font-medium text-gray-700 dark:text-gray-300">
            MERN Stack Developer
          </h2>
          
          <p className="text-lg text-gray-600 dark:text-gray-400 max-w-lg leading-relaxed font-light">
            I build modern, fast, and scalable web applications that turn ideas into reality. Specializing in high-performance digital experiences.
          </p>
          
          <div className="flex flex-wrap items-center gap-4 mt-6">
            <a href="#work" className="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-neon-purple to-neon-blue text-white px-8 py-3.5 rounded-full text-sm font-bold shadow-[0_0_20px_rgba(139,92,246,0.4)] hover:shadow-[0_0_30px_rgba(139,92,246,0.6)] hover:scale-105 transition-all duration-300">
              View My Work <ArrowRight size={18} />
            </a>
            <button onClick={downloadResume} className="inline-flex items-center justify-center gap-2 bg-white/10 dark:bg-white/5 border border-gray-200 dark:border-white/10 backdrop-blur-md text-gray-900 dark:text-white px-8 py-3.5 rounded-full text-sm font-bold hover:bg-gray-50 dark:hover:bg-white/10 transition-all duration-300">
              Download Résumé <Download size={18} />
            </button>
          </div>
        </motion.div>

        {/* Right Side - Profile Image (Desktop & Tablet) */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.2 }}
          className="relative w-full flex justify-center md:justify-end items-center order-2 mt-8 md:mt-0"
        >
          <div className="relative w-64 h-64 md:w-[380px] md:h-[380px] animate-float">
            <div className="absolute inset-0 rounded-full bg-gradient-to-tr from-neon-purple via-transparent to-neon-blue opacity-50 blur-xl animate-pulse-slow"></div>
            
            <div className="absolute inset-2 rounded-full p-1 bg-gradient-to-br from-white/40 to-white/5 backdrop-blur-sm z-10 border border-white/20 shadow-2xl overflow-hidden">
              <img 
                src="/profile.jpg" 
                alt="Abhishek Yadav" 
                className="w-full h-full object-cover rounded-full"
                onError={(e) => {
                  e.target.style.display = 'none';
                  e.target.nextSibling.style.display = 'flex';
                }}
              />
              <div className="hidden w-full h-full bg-[#111] flex-col items-center justify-center text-white/50 rounded-full">
                <Code size={48} className="mb-2 text-neon-purple" />
                <span className="text-xs font-mono">Image Missing</span>
              </div>
            </div>
            
            <motion.div 
              animate={{ y: [0, -15, 0] }} 
              transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
              className="absolute -right-2 top-10 glass-card px-4 py-2 rounded-2xl flex items-center gap-2 z-20 border border-white/20 shadow-[0_0_15px_rgba(59,130,246,0.3)]"
            >
              <div className="w-3 h-3 rounded-full bg-neon-blue animate-pulse"></div>
              <span className="text-sm font-bold text-gray-800 dark:text-white">React.js</span>
            </motion.div>
            
            <motion.div 
              animate={{ y: [0, 15, 0] }} 
              transition={{ duration: 5, repeat: Infinity, ease: "easeInOut", delay: 1 }}
              className="absolute -left-6 bottom-16 glass-card px-4 py-2 rounded-2xl flex items-center gap-2 z-20 border border-white/20 shadow-[0_0_15px_rgba(16,185,129,0.3)]"
            >
              <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>
              <span className="text-sm font-bold text-gray-800 dark:text-white">Node.js</span>
            </motion.div>
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
            <h2 className="text-xs font-semibold tracking-widest uppercase text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple mb-4">Biography</h2>
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
    icon: <Layout className="w-6 h-6 mb-4 text-neon-blue" />,
    items: ["React.js & Hooks", "JavaScript (ES6+)", "Tailwind CSS", "HTML5 & CSS3", "Bootstrap", "Responsive Design"]
  },
  {
    category: "Backend Architecture",
    icon: <Terminal className="w-6 h-6 mb-4 text-neon-blue" />,
    items: ["Node.js", "Express.js", "RESTful APIs", "JWT Authentication", "CRUD Operations", "API Integration"]
  },
  {
    category: "Database Management",
    icon: <Database className="w-6 h-6 mb-4 text-neon-blue" />,
    items: ["MongoDB", "Mongoose", "MySQL", "Data Modeling", "Query Optimization"]
  },
  {
    category: "Development Tools",
    icon: <Code2 className="w-6 h-6 mb-4 text-neon-blue" />,
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
          <h2 className="text-xs font-semibold tracking-widest uppercase text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple mb-4">Technical Arsenal</h2>
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
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-20"
        >
          <h2 className="text-xs font-semibold tracking-widest uppercase text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple mb-4">Selected Case Studies</h2>
          <h3 className="font-display text-3xl md:text-4xl text-gray-900 dark:text-white">Curated Digital Experiences.</h3>
        </motion.div>

        <div className="flex flex-col gap-24">
          {projects.map((project, index) => (
            <motion.div 
              key={index}
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
                <div className="flex flex-wrap gap-3 mb-2">
                  {project.tech.map((t, i) => (
                    <span key={i} className="text-xs font-semibold uppercase tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple">{t}</span>
                  ))}
                </div>
                <h4 className="font-display text-2xl md:text-3xl text-gray-900 dark:text-white">{project.title}</h4>
                <p className="text-gray-600 dark:text-gray-300 font-light leading-relaxed">
                  {project.description}
                </p>
                <div className="flex items-center gap-6 mt-4">
                  <a href={project.liveLink} className="text-sm font-medium border-b border-gray-900 dark:border-white hover:text-neon-blue hover:border-neon-blue dark:hover:text-neon-blue dark:hover:border-neon-blue transition-colors flex items-center gap-2 pb-1">
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
"""
}

for file_path, content in files.items():
    create_file(file_path, content)
    print(f"Updated: {file_path}")

print("\nSuccess: Desktop layout balanced side-by-side & unified electric blue text gradients applied.")
