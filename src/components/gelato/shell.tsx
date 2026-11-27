import { Link } from '@tanstack/react-router';
import { useState } from 'react';
import { ArrowUpRight, Menu, X, Leaf } from 'lucide-react';
import { Button } from '@/components/ui/button';
import logo from '@/assets/gelato-vero-logo-atual.png';
const links = [{ to: '/', label: 'Início' }, { to: '/sabores', label: 'Sabores' }, { to: '/sobre', label: 'Sobre nós' }, { to: '/contato', label: 'Contato' }] as const;
export function Header() {
 const [open, setOpen] = useState(false);
 return <header className="site-header"><div className="container header-inner"><Link to="/" aria-label="Gelato Vero — início" className="brand"><img src={logo} alt="Logo oficial Gelato Vero" /><span>GELATO <small>VERO</small></span></Link><nav className={open ? 'main-nav is-open' : 'main-nav'} aria-label="Menu principal">{links.map(link => <Link key={link.to} to={link.to} onClick={() => setOpen(false)} activeProps={{ className: 'active' }} activeOptions={{ exact: true }}>{link.label}</Link>)}</nav><Button asChild className="header-register"><Link to="/cadastro">Cadastre-se <ArrowUpRight /></Link></Button><Button className="menu-button" variant="ghost" size="icon" aria-label={open ? 'Fechar menu' : 'Abrir menu'} onClick={() => setOpen(!open)}>{open ? <X /> : <Menu />}</Button></div></header>;
}
export function Footer() {
 return <footer className="site-footer"><div className="container footer-main"><Link to="/" className="footer-brand">GELATO <span>VERO</span></Link><p>Feito com natureza.<br />Servido com carinho.</p><nav aria-label="Menu do rodapé">{links.map(link => <Link key={link.to} to={link.to}>{link.label}</Link>)}<Link to="/cadastro">Cadastro</Link></nav></div><div className="container footer-bottom"><span>© {new Date().getFullYear()} Gelato Vero · Projeto acadêmico ETEC</span><span><Leaf size={14} /> Sorvetes de polpa de frutas naturais</span></div></footer>;
}
