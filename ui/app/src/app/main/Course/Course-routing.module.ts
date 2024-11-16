import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseHomeComponent } from './home/Course-home.component';
import { CourseNewComponent } from './new/Course-new.component';
import { CourseDetailComponent } from './detail/Course-detail.component';

const routes: Routes = [
  {path: '', component: CourseHomeComponent},
  { path: 'new', component: CourseNewComponent },
  { path: ':id', component: CourseDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Course-detail-permissions'
      }
    }
  },{
    path: ':course_id/CourseMaterial', loadChildren: () => import('../CourseMaterial/CourseMaterial.module').then(m => m.CourseMaterialModule),
    data: {
        oPermission: {
            permissionId: 'CourseMaterial-detail-permissions'
        }
    }
},{
    path: ':course_id/Enrollment', loadChildren: () => import('../Enrollment/Enrollment.module').then(m => m.EnrollmentModule),
    data: {
        oPermission: {
            permissionId: 'Enrollment-detail-permissions'
        }
    }
},{
    path: ':course_id/Evaluation', loadChildren: () => import('../Evaluation/Evaluation.module').then(m => m.EvaluationModule),
    data: {
        oPermission: {
            permissionId: 'Evaluation-detail-permissions'
        }
    }
},{
    path: ':course_id/Feedback', loadChildren: () => import('../Feedback/Feedback.module').then(m => m.FeedbackModule),
    data: {
        oPermission: {
            permissionId: 'Feedback-detail-permissions'
        }
    }
},{
    path: ':course_id/InstructorAssignment', loadChildren: () => import('../InstructorAssignment/InstructorAssignment.module').then(m => m.InstructorAssignmentModule),
    data: {
        oPermission: {
            permissionId: 'InstructorAssignment-detail-permissions'
        }
    }
},{
    path: ':course_id/Schedule', loadChildren: () => import('../Schedule/Schedule.module').then(m => m.ScheduleModule),
    data: {
        oPermission: {
            permissionId: 'Schedule-detail-permissions'
        }
    }
}
];

export const COURSE_MODULE_DECLARATIONS = [
    CourseHomeComponent,
    CourseNewComponent,
    CourseDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CourseRoutingModule { }