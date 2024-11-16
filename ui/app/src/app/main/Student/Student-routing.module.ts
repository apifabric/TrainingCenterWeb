import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StudentHomeComponent } from './home/Student-home.component';
import { StudentNewComponent } from './new/Student-new.component';
import { StudentDetailComponent } from './detail/Student-detail.component';

const routes: Routes = [
  {path: '', component: StudentHomeComponent},
  { path: 'new', component: StudentNewComponent },
  { path: ':id', component: StudentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Student-detail-permissions'
      }
    }
  },{
    path: ':student_id/Enrollment', loadChildren: () => import('../Enrollment/Enrollment.module').then(m => m.EnrollmentModule),
    data: {
        oPermission: {
            permissionId: 'Enrollment-detail-permissions'
        }
    }
},{
    path: ':student_id/Evaluation', loadChildren: () => import('../Evaluation/Evaluation.module').then(m => m.EvaluationModule),
    data: {
        oPermission: {
            permissionId: 'Evaluation-detail-permissions'
        }
    }
},{
    path: ':student_id/Feedback', loadChildren: () => import('../Feedback/Feedback.module').then(m => m.FeedbackModule),
    data: {
        oPermission: {
            permissionId: 'Feedback-detail-permissions'
        }
    }
}
];

export const STUDENT_MODULE_DECLARATIONS = [
    StudentHomeComponent,
    StudentNewComponent,
    StudentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StudentRoutingModule { }