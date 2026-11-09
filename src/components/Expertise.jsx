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