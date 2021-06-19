import React from 'react'
import {Button, ButtonR} from '../ButtonElements'
import { 
    Column2, 
    ImgWrap,
    InfoContainer,
    InfoWrapper,
    InfoRow,
    Column1,
    TextWrapper,
    TopLine,
    Heading,
    Subtitle,
    BtnWrap,
    Img
} from './InfoElements'

const InfoSection = ({lightBg, 
    id, 
    imgStart, 
    topLine, 
    lightText, 
    headline, 
    darkText, 
    description, 
    buttonLabel, 
    img,
    primary,
    dark,
    dark2,   
    alt}) => {
    return (
        <>
         <InfoContainer lightBg={lightBg} id= {id}>
             <InfoWrapper>
                 <InfoRow imgStart={imgStart}>
                     <Column1>
                     <TextWrapper>
                         <TopLine>{topLine}</TopLine>
                         <Heading lightText={lightText}>{headline}</Heading>
                         <Subtitle darkText={darkText}>{description}</Subtitle>
                         <BtnWrap>
                             <ButtonR to="signup"
                             smooth={1}
                             duration={500}
                             spy={1}
                             exact="true"
                             offset={-80}
                             primary={primary ? 1 : 0}
                             dark={dark ? 1 : 0}
                             dark2={dark2 ? 1 :0}
                             >{buttonLabel} </ButtonR>
                         </BtnWrap>
                     </TextWrapper>
                     </Column1>
                     <Column2>
                     <ImgWrap>
                     <Img src={img} alt={alt}/>
                     </ImgWrap>
                     </Column2>
                 </InfoRow>
             </InfoWrapper>
             </InfoContainer>   
        </>
    )
}

export default InfoSection
