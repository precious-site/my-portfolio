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