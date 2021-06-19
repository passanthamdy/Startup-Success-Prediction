import React from 'react'
import {
    SidebarContainer, 
    Icon, 
    CloseIcon, 
    SidebarWrapper, 
    SidebarLink, 
    SidebarMenu, 
    SideBtnWrap, 
    SideBarRoute} from './Subelements'
const Sidebar = ({isOpen, toggle}) => {
    return (
        <SidebarContainer isOpen= {isOpen} onClick= {toggle}>
            <Icon onClick= {toggle}>
                <CloseIcon />
            </Icon>
            <SidebarWrapper>
                <SidebarMenu>
                    <SidebarLink to='/' onClick= {toggle}>
                        Home
                    </SidebarLink>
                    <SidebarLink to='/posts' onClick= {toggle}>
                        Startups
                    </SidebarLink>
                    <SidebarLink to='/investors' onClick= {toggle}>
                        Investors
                    </SidebarLink>
                    <SidebarLink to='/signup' onClick= {toggle}>
                        Signup
                    </SidebarLink>
                </SidebarMenu>
            <SideBtnWrap>
                <SideBarRoute to='/signin' onClick= {toggle}>
                    Sign in
                </SideBarRoute>
            </SideBtnWrap>
            </SidebarWrapper>
            
        </SidebarContainer>
    )
}

export default Sidebar
