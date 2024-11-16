import { MenuRootItem } from 'ontimize-web-ngx';

import { CertificateCardComponent } from './Certificate-card/Certificate-card.component';

import { CourseCardComponent } from './Course-card/Course-card.component';

import { CourseMaterialCardComponent } from './CourseMaterial-card/CourseMaterial-card.component';

import { EnrollmentCardComponent } from './Enrollment-card/Enrollment-card.component';

import { EvaluationCardComponent } from './Evaluation-card/Evaluation-card.component';

import { FeedbackCardComponent } from './Feedback-card/Feedback-card.component';

import { InstructorCardComponent } from './Instructor-card/Instructor-card.component';

import { InstructorAssignmentCardComponent } from './InstructorAssignment-card/InstructorAssignment-card.component';

import { RoomCardComponent } from './Room-card/Room-card.component';

import { ScheduleCardComponent } from './Schedule-card/Schedule-card.component';

import { StudentCardComponent } from './Student-card/Student-card.component';

import { TrainingCenterCardComponent } from './TrainingCenter-card/TrainingCenter-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Certificate', name: 'CERTIFICATE', icon: 'view_list', route: '/main/Certificate' }
    
        ,{ id: 'Course', name: 'COURSE', icon: 'view_list', route: '/main/Course' }
    
        ,{ id: 'CourseMaterial', name: 'COURSEMATERIAL', icon: 'view_list', route: '/main/CourseMaterial' }
    
        ,{ id: 'Enrollment', name: 'ENROLLMENT', icon: 'view_list', route: '/main/Enrollment' }
    
        ,{ id: 'Evaluation', name: 'EVALUATION', icon: 'view_list', route: '/main/Evaluation' }
    
        ,{ id: 'Feedback', name: 'FEEDBACK', icon: 'view_list', route: '/main/Feedback' }
    
        ,{ id: 'Instructor', name: 'INSTRUCTOR', icon: 'view_list', route: '/main/Instructor' }
    
        ,{ id: 'InstructorAssignment', name: 'INSTRUCTORASSIGNMENT', icon: 'view_list', route: '/main/InstructorAssignment' }
    
        ,{ id: 'Room', name: 'ROOM', icon: 'view_list', route: '/main/Room' }
    
        ,{ id: 'Schedule', name: 'SCHEDULE', icon: 'view_list', route: '/main/Schedule' }
    
        ,{ id: 'Student', name: 'STUDENT', icon: 'view_list', route: '/main/Student' }
    
        ,{ id: 'TrainingCenter', name: 'TRAININGCENTER', icon: 'view_list', route: '/main/TrainingCenter' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CertificateCardComponent

    ,CourseCardComponent

    ,CourseMaterialCardComponent

    ,EnrollmentCardComponent

    ,EvaluationCardComponent

    ,FeedbackCardComponent

    ,InstructorCardComponent

    ,InstructorAssignmentCardComponent

    ,RoomCardComponent

    ,ScheduleCardComponent

    ,StudentCardComponent

    ,TrainingCenterCardComponent

];