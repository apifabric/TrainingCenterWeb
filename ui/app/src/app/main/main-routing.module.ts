import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Certificate', loadChildren: () => import('./Certificate/Certificate.module').then(m => m.CertificateModule) },
    
        { path: 'Course', loadChildren: () => import('./Course/Course.module').then(m => m.CourseModule) },
    
        { path: 'CourseMaterial', loadChildren: () => import('./CourseMaterial/CourseMaterial.module').then(m => m.CourseMaterialModule) },
    
        { path: 'Enrollment', loadChildren: () => import('./Enrollment/Enrollment.module').then(m => m.EnrollmentModule) },
    
        { path: 'Evaluation', loadChildren: () => import('./Evaluation/Evaluation.module').then(m => m.EvaluationModule) },
    
        { path: 'Feedback', loadChildren: () => import('./Feedback/Feedback.module').then(m => m.FeedbackModule) },
    
        { path: 'Instructor', loadChildren: () => import('./Instructor/Instructor.module').then(m => m.InstructorModule) },
    
        { path: 'InstructorAssignment', loadChildren: () => import('./InstructorAssignment/InstructorAssignment.module').then(m => m.InstructorAssignmentModule) },
    
        { path: 'Room', loadChildren: () => import('./Room/Room.module').then(m => m.RoomModule) },
    
        { path: 'Schedule', loadChildren: () => import('./Schedule/Schedule.module').then(m => m.ScheduleModule) },
    
        { path: 'Student', loadChildren: () => import('./Student/Student.module').then(m => m.StudentModule) },
    
        { path: 'TrainingCenter', loadChildren: () => import('./TrainingCenter/TrainingCenter.module').then(m => m.TrainingCenterModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }